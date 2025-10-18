import openai

from aiogram import types
from loguru import logger

from config import model, io_API_key, SYSTEM_PROMT


client = openai.OpenAI(
    api_key = io_API_key,
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)


def handle_message(user_message: types.Message):
    logger.debug("Сообщение получено нейронкой")

    chat_history = [{
        "role": "system",
        "content": SYSTEM_PROMT
    }]   
    
    chat_history.append({
        "role": "user",
        "content": user_message
    })
    logger.info("Сообщение добавлено в историю чата")

    response = client.chat.completions.create(
        model=model,
        messages=chat_history,
        temperature=0.7,
        stream=False,
    )
    ai_answer = response.choices[0].message.content
    
    logger.success("Ответ сгенерирован")
    return ai_answer