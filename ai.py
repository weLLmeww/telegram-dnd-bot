import openai

from aiogram import types

from config import model, legend, io_API_key


client = openai.OpenAI(
    api_key = io_API_key,
    base_url = "https://api.intelligence.io.solutions/api/v1/"
)


def handle_message(user_message: types.Message):
    print(f"принято сообщение {user_message.text}...")
    
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": legend},
            {"role": "user", "content": user_message.text}
        ],
        temperature=0.7,
        stream=False,
    )
    bot_answer = completion.choices[0].message.content
    
    return bot_answer