import math

from datasource import Repository
from logic import term_frequency_calculator


class QueryProcessor:
    repository = Repository()

    def __init__(self, user_model):
        self.user = user_model
        self.query_text = user_model.query
        self.tf_list = [0.0] * (len(user_model.query.split(" ")))
        self.idf_list = [1.0] * (len(user_model.query.split(" ")))
        self.tf_by_idf_list = [0.0] * (len(user_model.query.split(" ")))
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
        documents_list = self.repository.fetch_all_requests()

        best_document_model = None
        # maximum cosine_similarity_value that we obtained
        best_document_model_value = 0.0

        split_request = self.query_text
        # loop through the list of all documents
        for document in documents_list:
            current_cosine_similarity_value = 0.0
            split_current_document = document.req.split(" ")
            for i in range(len(split_request)):
                # if a word exist in both of document and request then we use it (tf*idf value in cosine similarity
                # value)
                if split_request[i] in split_current_document:
                    request_tf_by_idf_value = self.tf_by_idf_list[i]
                    document_tf_by_idf_value = self.repository.fetch_req_word_by_req_id_word_id(
                        self.repository.find_word_by_string(split_request[i]).id, document.id).tfidf
                    current_cosine_similarity_value += request_tf_by_idf_value * document_tf_by_idf_value

            current_cosine_similarity_value /= (self.length_value * document.length)
            if current_cosine_similarity_value > best_document_model_value:
                best_document_model_value = current_cosine_similarity_value
                best_document_model = document

        return best_document_model

    def find_response_corresponding_request(self):
        document_model = self.cosine_similarity_calculator()
        # todo
        response_model = self.repository.fetch_response_by_request()

        return response_model
