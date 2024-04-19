import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
bot_token = os.getenv('BOT_TOKEN')
openai_id = os.getenv('OPENAI_ID')
host_stat = os.getenv('HOST_STAT')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
db_name = os.getenv('DATABASE_NAME')
