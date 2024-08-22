from aiogram import Router, types
from aiogram.filters import Command
from loguru import logger

from src.common.enums import TelegramCommand
from src.common.utils import stop_active_task
from src.common.utils.stop_active_task import active_tasks
from src.bot.root import RootRouter

from src.bot.resources.templates import STOP_SEND_IMAGE_SUCCESS, STOP_SEND_IMAGE_NULL

stop_images_command_router = Router()

def include_stop_images_command_router(root_router: RootRouter) -> None:
    root_router.include_router(stop_images_command_router)

@stop_images_command_router.message(Command(TelegramCommand.STOP_IMAGE_COMMAND))
async def stop_images_command(message: types.Message):
    user_id = message.chat.id
    if user_id in active_tasks:
        await stop_active_task(user_id)
        logger.info(f"User {user_id} stopped image sending.")
        await message.answer(text=STOP_SEND_IMAGE_SUCCESS)
    else:
        await message.answer(text=STOP_SEND_IMAGE_NULL)
