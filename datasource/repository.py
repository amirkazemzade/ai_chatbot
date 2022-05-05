from ai_chatbot.datasource.models.UserModel import UserModel
from ai_chatbot.datasource.provider import Provider


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
