
import constants
import telebot
from logic import QueryProcessor

ai_bot = telebot.TeleBot(constants.API_TOKEN)


@ai_bot.message_handler(commands=['start'])
def start(message):
    response = initialize_user(message)
    ai_bot.reply_to(message, response)


@ai_bot.message_handler(func=lambda m: True)
def all_messages(message):
    resend_message(message)


def initialize_user(message):
    processor = QueryProcessor()
    return processor.user_start(message.from_user)


def resend_message(message):
    ai_bot.reply_to(message, message.text)


ai_bot.polling()
