import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.admin_private import admin_private_router

ALLOWED_UPDATES = ['message']

bot = Bot(token=os.getenv('TOKEN'))


dp = Dispatcher()
dp.include_routers(user_private_router, admin_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())