from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.bot.init_bot import bot
from src.bot.root_router import build_root_router

__all__ = [
    "bot",

]

