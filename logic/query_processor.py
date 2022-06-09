import math

from datasource import Repository
from logic import term_frequency_calculator
from telebot import types
from datasource.models import ProductModel


class QueryProcessor:

    def __init__(self):
        self.repository = Repository()
        self.user_id = -1
        self.shopping_list_id = -1
        self.last_response = ""
        self.last_product = None
        self.repository = Repository()

    def user_start(self, user_telegram_model: types.User):
        user_id = self.create_user(user_telegram_model.id)
        self.user_id = user_id
        user_shopping_list_id = self.create_user_shopping_list(user_id)
        self.shopping_list_id = user_shopping_list_id
        return "{} سلام".format(user_telegram_model.first_name)

    def create_user(self, user_telegram_id):
        user_model = self.repository.fetch_user_by_tel_id(user_telegram_id)
        if user_model is None:
            user_id = self.repository.insert_user(user_telegram_id)
            return user_id
        else:
            return user_model.id

    def create_user_shopping_list(self, user_id):
        user_shopping_list = self.repository.fetch_user_shop_lists(user_id)
        if (user_shopping_list is None) or (len(user_shopping_list) == 0):
            shop_list_id = self.repository.insert_shop_list(user_id)
            return shop_list_id
        else:
            return user_shopping_list[0].id

    # this function calls when a query come
    def parameter_calculator(self, user_telegram_model: types.User, message: str):
        if self.last_response == "چه کالایی؟":
            is_product_exist_in_db = self.repository.fetch_product_by_name(message)
            if is_product_exist_in_db is None:
                product = ProductModel(name=message)
                self.repository.insert_product(product)
                self.last_product = product
            else:
                self.last_product = is_product_exist_in_db
            response = "چه مقدار؟"
            self.last_response = response
            return response
        elif self.last_response == "چه مقدار؟":
            # todo how to add a product into database
            # self.add_product_to_user_shopping_list(user_model.id, user_model.query)

            self.repository.insert_shop_list_content(self.shopping_list_id, self.last_product.id, message)

            response = "این کالا به سبد خرید شما اضافه شد."
            return response
        else:
            tf_list = self.tf_calculator(message)
            idf_list = self.idf_calculator(message)
            tf_by_idf_list = self.tf_by_idf_calculator(message, tf_list, idf_list)
            length = self.length_calculator(tf_by_idf_list)
            response_model = self.find_response_corresponding_request(message, tf_by_idf_list, length)

            self.last_response = response_model.resp

    def tf_calculator(self, query_text):
        tf_list = [0.0] * (len(query_text.split(" ")))
        request = query_text
        split_requests = request.split(" ")

        # calculating tf value for all word that this request has
        for i in range(len(split_requests)):
            tf_value = term_frequency_calculator.term_frequency(split_requests[i], request)
            tf_list[i] = tf_value

        return tf_list

    def idf_calculator(self, query_text):
        idf_list = [1.0] * (len(query_text.split(" ")))
        request = query_text
        split_requests = request.split(" ")

        # calculating idf value for all word that this request has
        for i in range(len(split_requests)):
            current_word = split_requests[i]
            current_word_model = self.repository.find_word_by_string(current_word)
            idf_value = 1.0
            if current_word_model is None:
                idf_list[i] = idf_value
            else:
                idf_value = current_word_model.idf
                idf_list[i] = idf_value
        return idf_list

    def tf_by_idf_calculator(self, query_text, tf_list, idf_list):
        tf_by_idf_list = [0.0] * (len(query_text.split(" ")))
        for i in range(len(tf_by_idf_list)):
            tf_by_idf_list[i] = tf_list[i] * idf_list[i]
        return tf_by_idf_list

    def length_calculator(self, tf_by_idf_list):
        square_value = 0.0
        for tf_idf in tf_by_idf_list:
            square_value += tf_idf ** 2

        return math.sqrt(square_value)

    def cosine_similarity_calculator(self, query_text, tf_by_idf_list, length_value):
        documents_list = self.repository.fetch_all_requests()

        best_document_model = None
        # maximum cosine_similarity_value that we obtained
        best_document_model_value = 0.0

        split_request = query_text
        # loop through the list of all documents
        for document in documents_list:
            current_cosine_similarity_value = 0.0
            split_current_document = document.req.split(" ")
            for i in range(len(split_request)):
                # if a word exist in both of document and request then we use it (tf*idf value in cosine similarity
                # value)
                if split_request[i] in split_current_document:
                    request_tf_by_idf_value = tf_by_idf_list[i]
                    document_tf_by_idf_value = self.repository.fetch_req_word_by_req_id_word_id(
                        self.repository.find_word_by_string(split_request[i]).id, document.id).tfidf
                    current_cosine_similarity_value += request_tf_by_idf_value * document_tf_by_idf_value

            current_cosine_similarity_value /= (length_value * document.length)
            if current_cosine_similarity_value > best_document_model_value:
                best_document_model_value = current_cosine_similarity_value
                best_document_model = document

        return best_document_model

    def find_response_corresponding_request(self, query_text, tf_by_idf_list, length_value):
        document_model = self.cosine_similarity_calculator(query_text, tf_by_idf_list, length_value)
        response_model = self.repository.fetch_response_by_req_id(document_model.id)
        return response_model[0]

    def add_product_to_user_shopping_list(self, user_id, product_id):
        self.repository.insert_shop_list_content(user_id, product_id)
