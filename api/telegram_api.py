import constants
import telebot
from logic import logic

ai_bot = telebot.TeleBot(constants.API_TOKEN)


@ai_bot.message_handler(commands=['start'])
def say_hello(message):
    ai_bot.reply_to(message, logic.user_start(message.from_user))


@ai_bot.message_handler(func=lambda m: True)
def send_message_again(message):
    ai_bot.reply_to(message, message.text)


ai_bot.polling()
