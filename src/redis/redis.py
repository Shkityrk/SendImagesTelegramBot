from aiogram.fsm.storage.redis import RedisStorage

from src.common.config import REDIS_HOST, REDIS_PORT

__all__=[
    "REDIS_URL",
    "storage",
]
# Формируем URL подключения к Redis
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'

# Создаем соединение с Redis
storage = RedisStorage.from_url(REDIS_URL)