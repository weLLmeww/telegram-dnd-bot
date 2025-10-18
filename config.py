import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.getenv('TOKEN')
io_API_key = os.getenv('API_KEY')
model = os.getenv('MODEL')
promt = os.getenv('PROMT')