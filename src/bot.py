import time
from telebot import TeleBot
from config import bot
from log.logger_config import logger
from handlers import handlers


if __name__ == "__main__":
    logger.info("Bot Started!")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        logger.error(f"Bot Crashed: {e}")
        time.sleep(2)
        logger.info("Bot Restarted!")
        bot.polling(none_stop=True)
