import openai

from aiogram import types
from loguru import logger

from config import model, promt, io_API_key


client = openai.OpenAI(
    api_key = io_API_key,
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)


def handle_message(user_message: types.Message):
    logger.debug(f"Сообщение от пользователя: {user_message.text}")

    chat_history = [{
        "role": "system",
        "content": promt
    }]

    chat_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model=model,
        messages=chat_history,
        temperature=0.7,
        stream=False,
    )
    ai_answer = response.choices[0].message.content
    
    logger.debug(ai_answer)
    
    return ai_answer