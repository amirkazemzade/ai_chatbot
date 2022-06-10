import constants
import telebot
from logic import QueryProcessor

ai_bot = telebot.TeleBot(constants.API_TOKEN)


@ai_bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    response = initialize_user(message)
    ai_bot.reply_to(message, response)


@ai_bot.message_handler(func=lambda m: True)
def all_messages(message: telebot.types.Message):
    response = response_to_message(message)
    ai_bot.reply_to(message, response)


def initialize_user(message: telebot.types.Message):
    processor = QueryProcessor()
    return processor.user_start(message.from_user)


def response_to_message(message: telebot.types.Message):
    processor = QueryProcessor()
    return processor.parameter_calculator(message.from_user, message.text)


ai_bot.polling()
