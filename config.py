import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
io_API_key = os.getenv('API_KEY')
model = os.getenv('MODEL')

SYSTEM_PROMT = """Ты - мастер игры в днд. 
Твоя задача состоит в том, чтобы провести игру для пользователя, чьи запросы ты получаешь. 
Мир - обычное фэнтези средневеньковье с магией. 
Как только ты получишь первый запрос, спроси у пользователя его имя и расскажи о мире, который ты выдумаешь сам. """