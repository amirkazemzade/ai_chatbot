from telebot import types


# TODO: this is just for test change it!
def user_start(user_id: types.User) -> str:
    return f'Hello {user_id}'
