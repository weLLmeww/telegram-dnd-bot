from aiogram import types, Router
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply_keyboard import admin_kb

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

@admin_router.message(Command("admin"))
async def admin_cmd(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=admin_kb)