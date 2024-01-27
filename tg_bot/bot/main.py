import asyncio
import logging
import os

from aiogram import Bot, Dispatcher

from utils.commands import set_commands
from handlers import start, user_mark

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher()

dp.include_routers(start.router_start, user_mark.router_command)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
