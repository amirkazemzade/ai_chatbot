import sqlite3

from ai_chatbot.datasource.models.UserModel import UserModel


class Provider:
    def __init__(self):
        self.path = 'database.sqlite'
        self.connection = sqlite3.connect(self.path)

    # user functions
    def insert_user(self, tel_id: int) -> int:
        cursor = self.connection.cursor()
        query = f'insert into user (tel_id) values ("{tel_id}")'
        cursor.execute(query)
        self.connection.commit()
        userId = cursor.lastrowid
        cursor.close()
        return userId

    def fetch_all_users(self) -> list[UserModel]:
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        query = 'select * from user'
        users = []
        for row in cursor.execute(query):
            users.append(UserModel(row[0], row[1], row[2]))
        return users

    def fetch_user_by_tel_id(self, tel_id: int) -> UserModel:
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        query = f'select * from user where tel_id={tel_id}'
        cursor.execute(query)
        userData = cursor.fetchone()
        return UserModel(userData[0], userData[1], userData[2])

    def fetch_user_by_index_id(self, index_id: int):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        query = f'select * from user where id={index_id}'
        cursor.execute(query)
        userData = cursor.fetchone()
        return UserModel(userData[0], userData[1], userData[2])
