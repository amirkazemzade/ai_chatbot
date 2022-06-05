import math
from telebot import types

# term_frequency : tf
# term : word
# document : sentence
from datasource.models import RequestModel


def term_frequency(term, document):
    normalized_document = document.lower().split()
    return normalized_document.count(term.lower()) / float(len(normalized_document))


# inverse_document_frequency : idf
# term : word
def inverse_document_frequency(term, list_of_all_document: list[RequestModel]):
    num_of_document_with_this_term = 0
    for doc in list_of_all_document:
        if term.lower() in doc.req.lower().split():
            num_of_document_with_this_term += 1

    if num_of_document_with_this_term > 0:
        return 1.0 + math.log(float(len(list_of_all_document)) / num_of_document_with_this_term)
    else:
        return 1.0


# we need tf * idf of each document to calculate length of document-vector
# tf_idf_of_document : this is a list of tf * idf of each term (word) in document
def length_calculator(tf_idf_of_document):
    square_value = 0.0
    for tf_idf in tf_idf_of_document:
        square_value += tf_idf ** 2

    return math.sqrt(square_value)


# document_vector : list of all tf * idf related to this document
# length of two parameter (document_vector, query_vector) should be same. (equal the number of all word that we have)
# for each term (word) that doesn't exist in the vector, we put 0 value in the equation
def cosine_similarity_calculator(document_vector, query_vector):
    dot_product = 0.0
    for i in range(len(document_vector)):
        dot_product += document_vector[i] * query_vector[i]

    return dot_product / (length_calculator(document_vector) * length_calculator(query_vector))


# TODO: this is just for test change it!
def user_start(user_id: types.User) -> str:
    return f'Hello {user_id}'
