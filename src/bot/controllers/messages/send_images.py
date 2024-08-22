import asyncio

from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

from loguru import logger

from src.redis.redis import storage
from src.common.enums import TelegramCommand

from src.bot.root import RootRouter
from src.bot.resources.templates import SEND_IMAGE_NULL_PROMPT

__all__ = [
    "include_send_img_command_router",
]

from src.common.utils import stop_active_task
from src.common.utils.stop_active_task import active_tasks
from src.parcer.send_img import send_images_task

send_img_command_router = Router()

def include_send_img_command_router(root_router: RootRouter) -> None:
    root_router.include_router(send_img_command_router)

@send_img_command_router.message(Command(TelegramCommand.SEND_IMAGE_COMMAND))
async def send_images_command(message: types.Message):
    user_id = message.chat.id
    search_prompt = await storage.redis.get(f'search_prompt:{user_id}')
    if search_prompt:
        logger.info(f"User {message.from_user.id} start send images successful.")
        await stop_active_task(user_id)
        task = asyncio.create_task(send_images_task(message.chat.id, search_prompt.decode()))
        active_tasks[user_id] = task
    else:
        await message.answer(text=SEND_IMAGE_NULL_PROMPT)

