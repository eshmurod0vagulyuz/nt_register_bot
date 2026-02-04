import asyncio
import logging

from aiogram import Bot, Dispatcher

from core.config import BOT_TOKEN, DEVELOPER_ID
from handlers import include_routers
from middlewares.language import setup_middleware
from utils.queries import create_tables

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def startup(bot: Bot):
    await create_tables()
    text = "Bot start to work"
    logging.info(text)
    await bot.send_message(chat_id=DEVELOPER_ID, text=text)


async def shutdown(bot: Bot):
    text = "Bot stopped"
    logging.info(text)
    await bot.send_message(chat_id=DEVELOPER_ID, text=text)


async def main():
    main_router = include_routers()
    dp.include_router(main_router)

    setup_middleware(dp)

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    asyncio.run(main())
