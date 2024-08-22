from aiogram import Bot
from aiogram.enums import ParseMode
from src.common.config import API_TOKEN

bot = Bot(API_TOKEN, parse_mode=ParseMode.HTML)  # Initializing the Bot
