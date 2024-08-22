import asyncio

from aiogram import Dispatcher, Bot
from loguru import logger

from src.bot.root_router import build_root_router
from src.common.config import configurate_logger, API_TOKEN
from src.redis import storage

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=storage)


async def main() -> None:
    configurate_logger()
    logger.info("LOGGER CONFIGURED")

    logger.info("STARTING THE BOT...")

    # Построение и регистрация RootRouter
    root_router = build_root_router()
    dp.include_router(root_router)  # Добавляем кастомный роутер в Dispatcher

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)  # Запуск polling


if __name__ == "__main__":
    asyncio.run(main())
