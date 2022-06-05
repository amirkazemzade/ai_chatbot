import math


# we need tf * idf of each document to calculate length of document-vector
# tf_idf_of_document : this is a list of tf * idf of each term (word) in document
def length_calculator(tf_idf_of_document):
    square_value = 0.0
    for tf_idf in tf_idf_of_document:
        square_value += tf_idf ** 2

    return math.sqrt(square_value)
