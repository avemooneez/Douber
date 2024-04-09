import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
bot_token = os.getenv('BOT_TOKEN')
sber_id = os.getenv('SBER_ID')