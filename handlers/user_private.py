import os
import openai

from aiogram import types, Router
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

legend = os.getenv('LEGEND')
user_private_router = Router()


client = openai.OpenAI(
    api_key = os.getenv('API_KEY'),
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    print("поступила команда старт")
    await message.answer("Это команда старт")

@user_private_router.message()
async def handle_message(message: types.Message):
    print(f"поступило сообщение {message.text}")
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-0528",
        messages=[
            {"role": "system", "content": legend},
            {"role": "user", "content": message.text},
        ],
        temperature=0.7,
        stream=False,
    )
    answer = response.choices[0].message.content
    print(answer)
    await message.answer(answer)