from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from loguru import logger

from src.common.enums import TelegramCommand
from src.bot.resources.templates import START_COMMAND_TEMPLATE
from src.bot.root import RootRouter


__all__ = [
    "include_start_command_router",
]

start_command_router = Router()


def include_start_command_router(root_router: RootRouter) -> None:
    if start_command_router.parent_router is None:
        root_router.include_router(start_command_router)
    else:
        logger.warning("Router 'start_command_router' is already attached.")


@start_command_router.message(Command(TelegramCommand.START_COMMAND))
async def start_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer(text=START_COMMAND_TEMPLATE, parse_mode=ParseMode.HTML)
