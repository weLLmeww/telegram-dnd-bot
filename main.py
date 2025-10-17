import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


from handlers.user_router import user_router
from common.bot_commands_list import private

ALLOWED_UPDATES = ['message']

bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode="HTML"))

dp = Dispatcher()
dp.include_routers(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands = private, scope=types.BotCommandScopeAllPrivateChats())
    print("бот запущен")
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())