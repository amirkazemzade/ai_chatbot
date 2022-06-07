import math

from datasource import Repository
from logic import term_frequency_calculator


class QueryProcessor:
    repository = Repository()

    def __init__(self, user_model, query):
        self.user = user_model
        self.query_text = query
        self.tf_list = [0.0] * (len(query.split(" ")))
        self.idf_list = [1.0] * (len(query.split(" ")))
        self.tf_by_idf_list = [0.0] * (len(query.split(" ")))
        self.length_value = 0.0

    def tf_calculator(self):
        request = self.query_text
        split_requests = request.split(" ")

        # calculating tf value for all word that this request has
        for i in range(len(split_requests)):
            tf_value = term_frequency_calculator.term_frequency(split_requests[i], request)
            self.tf_list[i] = tf_value

    def idf_calculator(self):
        request = self.query_text
        split_requests = request.split(" ")

        # calculating idf value for all word that this request has
        for i in range(len(split_requests)):
            current_word = split_requests[i]
            current_word_model = self.repository.find_word_by_string(current_word)
            idf_value = 1.0
            if current_word_model is None:
                self.idf_list[i] = idf_value
            else:
                idf_value = current_word_model.idf
                self.idf_list[i] = idf_value

    def tf_by_idf_calculator(self):
        for i in range(len(self.tf_by_idf_list)):
            self.tf_by_idf_list[i] = self.tf_list[i] * self.idf_list[i]

    def length_calculator(self):
        square_value = 0.0
        for tf_idf in self.tf_by_idf_list:
            square_value += tf_idf ** 2

        self.length_value = math.sqrt(square_value)

    def cosine_similarity_calculator(self):
        # todo : we need calculate the cosine_similarity_value for each document that we have
        # for example cosine_similarity(d1 , query) , ....



        pass