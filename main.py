import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from loguru import logger

from routers.user_router import user_router
from common.bot_commands_list import private

from config import BOT_TOKEN
from database.sqlite import init_db


ALLOWED_UPDATES = ['text_message']

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="Markdown"))

dp = Dispatcher()
dp.include_routers(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands = private, scope=types.BotCommandScopeAllPrivateChats())
    await init_db()
    logger.success("Бот запущен")
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())