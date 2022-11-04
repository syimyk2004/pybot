import telebot
from decouple import config
bot = telebot.TeleBot(config("TOKEN_BOT"))



@bot.message_handler(command=["start", "привет"])
def get_start_message(message):
    full_name = f"{message.from_user.user_name}!!!"
    text = f"Welcome {full_name}"
    bot.send_message(message.chat.id, text)







bot.polling()