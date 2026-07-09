import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import settings
from handlers import common

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()
    
    # Регистрация роутеров
    dp.include_router(common.router)
    
    logging.info("Starting bot orchestrator...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())