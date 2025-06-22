import os
import openai

from aiogram import types, Router
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = openai.OpenAI(
    api_key = os.getenv('API_KEY'),
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)

def handle_message(user_message: types.Message = "", system_message: str = ""):
    print(f"принято сообщение {user_message.text}...")
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-0528",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message.text},
        ],
        temperature=0.7,
        stream=False,
    )
    bot_answer = response.choices[0].message.content
    print(f"cформирован ответ: \n {bot_answer}")
    
    answer = bot_answer.split("</think>")[1]
    return answer