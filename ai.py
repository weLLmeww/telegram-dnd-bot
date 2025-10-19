from openai import AsyncOpenAI

from loguru import logger
from typing import List, Tuple, Dict

from database.sqlite import get_history
from config import model, io_API_key, SYSTEM_PROMT


client = AsyncOpenAI(
    api_key = io_API_key,
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)

async def build_messages(user_id: int) -> List[Dict[str, str]]:
    logger.debug("Начало сборки запроса к нейросети...")
    try:
        messages: List[Dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMT}]

        history: List[Tuple[str, str]] = await  get_history(user_id)
        for role, content in history:
            messages.append({"role": role, "content": content})
        logger.debug("Запрос к нейросети собран")
        return messages
    except Exception as e:
        logger.error(f"Ошибка сборки запроса: {e}")


async def handle_message(messages: List[Dict[str, str]]):
    logger.debug("Обработка нейронкой...")
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            stream=False,
        )
        ai_answer = response.choices[0].message.content
        
        logger.success("Ответ сгенерирован успешно")
        if "</think>" in ai_answer:
            return ai_answer.split("</think>")[1]
        else:
            return ai_answer
    except Exception as e:
        logger.error(f"Ошибка обработки сообщения: {e}")