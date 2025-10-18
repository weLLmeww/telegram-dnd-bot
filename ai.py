import openai

from loguru import logger
from typing import List, Tuple, Dict

from database.db import get_history
from config import model, io_API_key, SYSTEM_PROMT


client = openai.OpenAI(
    api_key = io_API_key,
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)

def build_messages(user_id: int) -> List[Dict[str, str]]:
    messages: List[Dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMT}]

    history: List[Tuple[str, str]] = get_history(user_id)
    for role, content in history:
        messages.append({"role": role, "content": content})

    return messages


def handle_message(messages: List[Dict[str, str]]):
    logger.debug("Обработка нейронкой...")

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        stream=False,
    )
    ai_answer = response.choices[0].message.content
    
    logger.success("Ответ сгенерирован")
    if "</think>" in ai_answer:
        return ai_answer.split("</think>")[1]
    else:
        return ai_answer