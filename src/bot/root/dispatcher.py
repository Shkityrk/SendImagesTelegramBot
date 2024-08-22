from aiogram import Bot, Dispatcher

from src.common.config import API_TOKEN
from src.redis import storage

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)