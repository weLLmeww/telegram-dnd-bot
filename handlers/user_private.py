from aiogram import types, Router
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from ai import handle_message
from keyboards import reply_keyboard
user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    print("поступила команда старт")
    await message.answer("Это команда старт", reply_markup=reply_keyboard.start_kb)   

@user_private_router.message()
async def user_answer(message: types.Message):
    print(f"поступило сообщение {message.text}")
    answer = handle_message(message)
    print(f"выдан ответ: \n{answer}")
    await message.answer(answer, parse_mode="Markdown")