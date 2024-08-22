import asyncio

import requests
from loguru import logger
import xml.etree.ElementTree as ET

from src.redis.redis import storage
from src.bot import bot
from src.common.config import FOLDER_ID, API_YANDEX

__all__=[
    "get_xml",
    "parse_xml",
    "create_urls",
    "parse_xml",
    "send_images_task",
]

def get_xml(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f'Error getting XML: {e}')
        return None

def parse_xml(xml_data):
    try:
        root = ET.fromstring(xml_data)
        urls = []
        for doc in root.findall('.//doc'):
            url_elem = doc.find('.//url')
            if url_elem is not None:
                urls.append(url_elem.text)
        return urls
    except ET.ParseError as e:
        logger.error(f'Error parsing XML: {e}')
        return []

async def create_urls(search_prompt):
    '''Use Yandex API to create urls based on search_prompt
    see more at
    https://yandex.cloud/ru/docs/search-api/concepts/pic-search?utm_referrer=https%3A%2F%2Fyandex.ru%2F
    (u need yandex.cloud account + service account(FOLDER_ID) + API(API_YANDEX))'''
    xml_url_alias = 'https://yandex.ru/images-xml?folderid=' + FOLDER_ID + '&apikey=' + API_YANDEX + '&isize=large&groupby=attr=ii.groups-on-page=60&p=2&fyandex=1&itype=jpg&icolor=color&text='
    xml_url = xml_url_alias + search_prompt
    xml_data = get_xml(xml_url)

    return list(set(parse_xml(xml_data)))

async def send_images_task(chat_id, search_prompt ):
    image_urls = await create_urls(search_prompt)
    if not image_urls:
        return

    user_id = chat_id # откуда взять id юзера?? - будем считать что id юзера равно id чата)) так что для бесед не сгодится(
    # вообще, сделать при старте бота геттер user_id на основе chat_id, надеюсь, я когда нибудь сделаю так

    try:
        sleep_time = int(await storage.redis.get(f'sleep_time:{user_id}'))
    except Exception as e:
        sleep_time = 10
        logger.info(f'User not set sleep_time, so sleep_time=10')

    for image_url in image_urls:
        try:
            await bot.send_photo(chat_id, photo=image_url)

            if sleep_time and sleep_time > 1:
                await asyncio.sleep(sleep_time)
            else:
                await asyncio.sleep(2)
            logger.info(sleep_time)
        except Exception as e:
            logger.error(f'Error send img: {e}')
