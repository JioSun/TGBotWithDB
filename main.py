import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.routers import router
from database.db_main import db_init

# Bot token can be obtained via https://t.me/BotFather
load_dotenv()
TOKEN = getenv('BOT_TOKEN')

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.include_router(router)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN , default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    db_init()
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())