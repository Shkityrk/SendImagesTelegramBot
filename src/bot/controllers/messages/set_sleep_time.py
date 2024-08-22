from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from loguru import logger

from src.common.utils import CommandStates, stop_active_task
from src.common.enums import TelegramCommand

from src.redis.redis import storage

from src.bot.resources.templates import (
    SET_SLEEP_TIME_MESSAGE,
    SET_SLEEP_TIME_MESSAGE_SUCCESS,
    SET_SLEEP_TIME_MESSAGE_ERROR_ISNULL,
    SET_SLEEP_TIME_MESSAGE_ERROR_ISDIGIT,
    SET_SLEEP_TIME_MESSAGE_ERROR_ISNATURAL,
)
from src.bot.root import RootRouter

__all__ = [
    "include_set_sleep_time_command_router"
]

set_set_sleep_time_command_router = Router()


def include_set_sleep_time_command_router(root_router: RootRouter) -> None:
    root_router.include_router(set_set_sleep_time_command_router)


# Обработчик для команды /set_search

@set_set_sleep_time_command_router.message(Command(TelegramCommand.SET_SLEEP_TIME))
async def set_sleep_time_command(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    logger.info(f"User {user_id} used /sleep_time with message: {message.text}")

    # Команда пользователя
    command_part = message.text.strip().split(' ', 1) if len(message.text.split()) > 1 else []

    if len(command_part) < 2:
        await message.answer(text=SET_SLEEP_TIME_MESSAGE)
        await state.set_state(CommandStates.sleep_time)
    else:
        sleep_time = command_part[1].strip()
        await stop_active_task(user_id)
        await storage.redis.set(f'sleep_time:{user_id}', sleep_time)
        logger.info(f"sleep_time set for user {user_id}: {sleep_time}")
        await message.answer(text=SET_SLEEP_TIME_MESSAGE_SUCCESS + sleep_time)

@set_set_sleep_time_command_router.message(StateFilter(CommandStates.sleep_time))
async def process_set_sleep_time(message: types.Message, state: FSMContext):
    user_id = message.chat.id
    command_part = message.text.strip()
    if command_part is None:
        await message.answer(text=SET_SLEEP_TIME_MESSAGE_ERROR_ISNULL)
        return
    elif not command_part.isdigit():
        await message.answer(text=SET_SLEEP_TIME_MESSAGE_ERROR_ISDIGIT)
        return

    sleep_time = int(command_part)
    if sleep_time <= 0:
        await message.answer(text=SET_SLEEP_TIME_MESSAGE_ERROR_ISNATURAL)
        return

    await stop_active_task(user_id)
    await storage.redis.set(f'sleep_time:{user_id}', sleep_time)
    logger.info(f"Sleep time set for user {user_id}: {sleep_time}")


    await message.answer(text=SET_SLEEP_TIME_MESSAGE_SUCCESS + str(sleep_time))

    await state.clear()
