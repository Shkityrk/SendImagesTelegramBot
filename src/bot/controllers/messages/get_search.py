from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from loguru import logger

from src.bot.resources.templates import GET_SEARCH_MESSAGE_SUCCESS,GET_SEARCH_MESSAGE_ERROR, SET_SEARCH_MESSAGE_SUCCESS
from src.common.enums import TelegramCommand
from src.bot.root import RootRouter
from src.redis.redis import storage


get_search_command_router = Router()

def include_get_search_command_router(root_router: RootRouter) -> None:
    root_router.include_router(get_search_command_router)

@get_search_command_router.message(Command(TelegramCommand.GET_SEARCH_COMMAND))
async def get_search_command(message: types.Message):
    user_id = message.chat.id
    search_prompt = await storage.redis.get(f'search_prompt:{user_id}')
    if search_prompt:
        logger.info(f"User {message.from_user.id} get prompt successful.")
        await message.answer(text = (GET_SEARCH_MESSAGE_SUCCESS + search_prompt.decode()))
    else:
        logger.error(f"User {message.from_user.id} get prompt NOT successful.")
        await message.answer(text=GET_SEARCH_MESSAGE_ERROR, parse_mode=ParseMode.HTML)
