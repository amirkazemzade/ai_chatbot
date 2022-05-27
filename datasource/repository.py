from .models import *
from .provider import Provider


class Repository:

    # singleton implementation
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Repository, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.provider = Provider()

    # user functions
    def insert_user(self, tel_id: int) -> int:
        return self.provider.insert_user(tel_id)

    def fetch_all_users(self) -> list[UserModel]:
        return self.provider.fetch_all_users()

    def fetch_user_by_tel_id(self, tel_id: int) -> UserModel:
        return self.provider.fetch_user_by_tel_id(tel_id)

    def fetch_user_by_index_id(self, index_id: int) -> UserModel:
        return self.provider.fetch_user_by_index_id(index_id)

    # request functions
    def insert_request(self, req: str, created_by: int = None, length: float = None) -> int:
        return self.provider.insert_request(req, created_by, length)

    def fetch_all_requests(self) -> list[RequestModel]:
        return self.provider.fetch_all_requests()

    def fetch_request_by_id(self, req_id: int) -> RequestModel:
        return self.provider.fetch_request_by_id(req_id)

    def update_request(self, req: RequestModel):
        return self.provider.update_request(req)

    # response functions
    def insert_response(self, res: str) -> int:
        return self.provider.insert_response(res)

    def fetch_all_responses(self) -> list[ResponseModel]:
        return self.provider.fetch_all_responses()

    def fetch_response_by_id(self, res_id: int) -> ResponseModel:
        return self.provider.fetch_response_by_id(res_id)

    # shop list functions
    def insert_shop_list(self, user_id: int) -> int:
        return self.provider.insert_shop_list(user_id)

    def fetch_all_shop_lists(self) -> list[ShopListModel]:
        return self.provider.fetch_all_shop_lists()

    def fetch_user_shop_lists(self, user_id: int) -> list[ShopListModel]:
        return self.provider.fetch_user_shop_lists(user_id)

    def fetch_shop_list_by_id(self, shop_list_id: int) -> ShopListModel:
        return self.provider.fetch_shop_list_by_id(shop_list_id)
    
    # word functions
    def insert_word(self, word: WordModel) -> int:
        return self.provider.insert_word(word)

    def write_all_words(self, words: list[WordModel]):
        return self.provider.write_all_words(words)

    def update_word(self, word: WordModel):
        return self.provider.update_word(word)

    # req_word functions
    def insert_req_word(self, req_word: ReqWordModel) -> int:
        return self.provider.insert_req_word(req_word)

    def update_req_word(self, req_word: ReqWordModel):
        return self.provider.update_req_word(req_word)

    def update_all_req_words(self, req_words: list[ReqWordModel]):
        return self.provider.update_all_req_words(req_words)