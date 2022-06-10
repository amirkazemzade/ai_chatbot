import constants
import telebot
from logic import QueryProcessor

ai_bot = telebot.TeleBot(constants.API_TOKEN)
processor = QueryProcessor()


@ai_bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    response = initialize_user(message)
    ai_bot.reply_to(message, response)


@ai_bot.message_handler(func=lambda m: True)
def all_messages(message: telebot.types.Message):
    response_to_message(message)


def initialize_user(message: telebot.types.Message):
    return processor.user_start(message.from_user)


def response_to_message(message: telebot.types.Message):
    return processor.parameter_calculator(message.from_user, message.text)


ai_bot.polling()
