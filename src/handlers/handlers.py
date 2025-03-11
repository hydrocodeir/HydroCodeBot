from config import bot, ADMIN_CHAT_ID

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    if chat_id == ADMIN_CHAT_ID:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Hello! I'm a bot! {message.chat.id}"
        )