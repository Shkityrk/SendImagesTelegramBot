from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command

from loguru import logger
from src.common.enums import TelegramCommand
from src.bot.resources.templates import HELP_MESSAGE
from src.bot.root import RootRouter

__all__ = [
    "include_help_command_router",
]

help_command_router = Router()

def include_help_command_router(root_router: RootRouter) -> None:
    root_router.include_router(help_command_router)
@help_command_router.message(Command(TelegramCommand.HELP_COMMAND))
async def help_command(message: types.Message):
    logger.info(f"User {message.from_user.id} requested help.")
    await message.answer(text=HELP_MESSAGE, parse_mode=ParseMode.HTML)