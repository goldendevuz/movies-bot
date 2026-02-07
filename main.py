import asyncio
import logging
import sys

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import FSMI18nMiddleware, I18n
from dotenv import load_dotenv

from bot.handler import *
from bot.utils.settings import on_startup

load_dotenv()
import os

TOKEN = os.getenv('BOT_TOKEN')


async def main() -> None:
    i18n = I18n(path='locales', default_locale='en', domain='messages')
    dp.startup.register(on_startup)
    dp.update.middleware(FSMI18nMiddleware(i18n))
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
