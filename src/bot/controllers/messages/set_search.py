from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from loguru import logger

from src.common.utils import CommandStates
from src.redis.redis import storage
from src.common.enums import TelegramCommand
from src.bot.resources.templates import SET_SEARCH_MESSAGE, SET_SEARCH_MESSAGE_SUCCESS
from src.bot.root import RootRouter
from src.common.utils import stop_active_task

__all__ = [
    "include_set_search_command_router"
]

set_search_command_router = Router()


def include_set_search_command_router(root_router: RootRouter) -> None:
    root_router.include_router(set_search_command_router)


# Обработчик для команды /set_search
@set_search_command_router.message(Command(TelegramCommand.SET_SEARCH_COMMAND))
async def set_search_command(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    logger.info(f"User {user_id} used /set_search with message: {message.text}")

    command_parts = message.text.strip().split(' ', 1)

    if len(command_parts) < 2 or not command_parts[1].strip():
        # Если нет поискового запроса, просим ввести
        await message.answer(text=SET_SEARCH_MESSAGE, parse_mode=ParseMode.HTML)
        await state.set_state(CommandStates.waiting_for_prompt)
    else:
        # Если запрос сразу передан
        search_prompt = command_parts[1].strip()
        await stop_active_task(user_id)
        await storage.redis.set(f'search_prompt:{user_id}', search_prompt)
        logger.info(f"Set search prompt set for user {user_id}")
        await message.answer(text=SET_SEARCH_MESSAGE_SUCCESS+ search_prompt)


# Обработчик для ввода поискового запроса после команды
@set_search_command_router.message(StateFilter(CommandStates.waiting_for_prompt))
async def process_search_prompt(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    search_prompt = message.text.strip()

    if not search_prompt:
        await message.answer(text=SET_SEARCH_MESSAGE)
        return


    await stop_active_task(user_id)
    await storage.redis.set(f'search_prompt:{user_id}', search_prompt)
    logger.info(f"Set search prompt set for user {user_id}")

    await message.answer(text=SET_SEARCH_MESSAGE_SUCCESS + search_prompt)

    await state.clear()
