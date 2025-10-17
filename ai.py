import os
import openai

from aiogram import types

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

LEGEND = os.getenv('LEGEND')
MODEL = os.getenv('MODEL')

client = openai.OpenAI(
    api_key = os.getenv('API_KEY'),
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)


def handle_message(user_message: types.Message):
    print(f"принято сообщение {user_message.text}...")
    
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": LEGEND},
            {"role": "user", "content": user_message.text}
        ],
        temperature=0.7,
        stream=False,
    )
    bot_answer = completion.choices[0].message.content
    print(f"cформирован ответ: \n{bot_answer}")
    
    return bot_answer