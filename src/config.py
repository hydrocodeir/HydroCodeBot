import os
from dotenv import load_dotenv
from telebot import TeleBot


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)


BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID'))


bot = TeleBot(token=BOT_TOKEN)
