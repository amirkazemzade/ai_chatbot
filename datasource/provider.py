import sqlite3

from constants import ROOT_DIR
from .models import *


class Provider:
    def __init__(self):
        self.path = f'{ROOT_DIR}/database.sqlite'
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
        cursor = self.connection.cursor()
        query = 'select * from user'
        users = []
        for row in cursor.execute(query):
            users.append(UserModel(row[0], row[1], row[2]))
        cursor.close()
        return users

    def fetch_user_by_tel_id(self, tel_id: int) -> UserModel:
        cursor = self.connection.cursor()
        query = f'select * from user where tel_id={tel_id}'
        cursor.execute(query)
        user = UserModel(*cursor.fetchone())
        cursor.close()
        return user

    def fetch_user_by_index_id(self, index_id: int) -> UserModel:
        cursor = self.connection.cursor()
        query = f'select * from user where id={index_id}'
        cursor.execute(query)
        user = UserModel(*cursor.fetchone())
        cursor.close()
        return user

    # request functions
    def insert_request(self, req: str, created_by: int = None, length: float = None) -> int:
        cursor = self.connection.cursor()
        query = f'insert into request (req, created_by, length) values ("{req}", "{created_by}", "{length}")'
        cursor.execute(query)
        self.connection.commit()
        reqId = cursor.lastrowid
        cursor.close()
        return reqId

    def fetch_all_requests(self) -> list[RequestModel]:
        cursor = self.connection.cursor()
        query = 'select * from request'
        requests = []
        for row in cursor.execute(query):
            requests.append(RequestModel(*row))
        cursor.close()
        return requests

    def fetch_request_by_id(self, req_id: int) -> RequestModel:
        cursor = self.connection.cursor()
        query = f'select * from request where id={req_id}'
        cursor.execute(query)
        req = RequestModel(*cursor.fetchone())
        cursor.close()
        return req

    def update_request(self, request: RequestModel):
        cursor = self.connection.cursor()
        query = f'update request ' \
                f'set req="{request.req}", created_by="{request.createdBy}", created_at="{request.createdAt}" ' \
                f'where id="{request.id}" '
        cursor.execute(query)
        cursor.close()

    # response functions
    def insert_response(self, res: str) -> int:
        cursor = self.connection.cursor()
        query = f'insert into response (resp) values ("{res}")'
        cursor.execute(query)
        self.connection.commit()
        resId = cursor.lastrowid
        cursor.close()
        return resId

    def fetch_all_responses(self) -> list[ResponseModel]:
        cursor = self.connection.cursor()
        query = 'select * from response'
        responses = []
        for row in cursor.execute(query):
            responses.append(ResponseModel(*row))
        cursor.close()
        return responses

    def fetch_response_by_id(self, res_id: int) -> ResponseModel:
        cursor = self.connection.cursor()
        query = f'select * from response where id={res_id}'
        cursor.execute(query)
        res = ResponseModel(*cursor.fetchone())
        cursor.close()
        return res

    # shop list functions
    def insert_shop_list(self, user_id: int) -> int:
        cursor = self.connection.cursor()
        query = f'insert into shop_list (user_id) values ("{user_id}")'
        cursor.execute(query)
        self.connection.commit()
        shopListId = cursor.lastrowid
        cursor.close()
        return shopListId

    def fetch_all_shop_lists(self) -> list[ShopListModel]:
        cursor = self.connection.cursor()
        query = 'select * from shop_list'
        shopLists = []
        for row in cursor.execute(query):
            shopLists.append(ShopListModel(*row))
        cursor.close()
        return shopLists

    def fetch_user_shop_lists(self, user_id: int) -> list[ShopListModel]:
        cursor = self.connection.cursor()
        query = f'select * from shop_list where user_id={user_id} order by created_at desc'
        shopLists = []
        for row in cursor.execute(query):
            shopLists.append(ShopListModel(*row))
        cursor.close()
        return shopLists

    def fetch_shop_list_by_id(self, shop_list_id: int) -> ShopListModel:
        cursor = self.connection.cursor()
        query = f'select * from shop_list where id={shop_list_id}'
        cursor.execute(query)
        shopList = ShopListModel(*cursor.fetchone())
        cursor.close()
        return shopList

    # word functions
    def insert_word(self, word: WordModel) -> int:
        cursor = self.connection.cursor()
        query = f'insert into word (word, idf, is_product) values ("{word.word}", "{word.idf}", "{word.is_product}")'
        cursor.execute(query)
        self.connection.commit()
        wordId = cursor.lastrowid
        cursor.close()
        return wordId

    def write_all_words(self, words: list[WordModel]):
        for word in words:
            self.insert_word(word)

    def update_word(self, word: WordModel):
        cursor = self.connection.cursor()
        query = f'update word set ' \
                f'word="{word.word}", idf="{word.idf}", is_product="{word.is_product}" ' \
                f'where id="{word.id}" '
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    # req_word functions
    def insert_req_word(self, req_word: ReqWordModel) -> int:
        cursor = self.connection.cursor()
        query = f'insert into req_word (req_id, word_id, tf, tfidf) ' \
                f'values("{req_word.req_id}", "{req_word.word_id}", "{req_word.tf}", "{req_word.tfidf}")'
        cursor.execute(query)
        self.connection.commit()
        reqWordId = cursor.lastrowid
        cursor.close()
        return reqWordId

    def update_req_word(self, req_word: ReqWordModel):
        cursor = self.connection.cursor()
        query = f'update req_word set tf="{req_word.tf}", tfidf="{req_word.tfidf}"'
        cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def update_all_req_words(self, req_words: list[ReqWordModel]):
        cursor = self.connection.cursor()
        for req_word in req_words:
            self.update_req_word(req_word)