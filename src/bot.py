import time
from telebot import TeleBot
from config import bot
from log.logger_config import logger
from handlers import handlers


if __name__ == "__main__":
    print("Bot Started :)")
    logger.info("Bot Started!")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print("Bot Crashed :(")
        logger.error(f"Bot Crashed: {e}")
        time.sleep(2)
        print("Bot Crashed :|")
        logger.info("Bot Restarted!")
        bot.polling(none_stop=True)
