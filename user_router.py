from aiogram import types, Router
from loguru import logger

from database.db import add_message
from ai import build_messages, handle_message

user_router = Router()


@user_router.message()
async def answer(message: types.Message):
    logger.info(f"Сообщение от пользователя: {message.text}")
    user_id = message.from_user.id
    user_text = message.text.strip()

    add_message(user_id, role="user", content=user_text)
    messages = build_messages(user_id)

    answer = handle_message(messages)
    
    add_message(user_id, role="assistant", content=answer)
    await message.answer(answer)
    logger.success(f"Ответ отправлен")
