import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
sber_id = os.getenv('SBER_ID')