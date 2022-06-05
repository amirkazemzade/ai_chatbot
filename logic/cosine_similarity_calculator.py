from logic import length_parameter_calculator


# document_vector : list of all tf * idf related to this document length of two parameter (document_vector,
# query_vector) should be same. (equal the number of all word that we have) for each term (word) that doesn't
# exist in the vector, we put 0 value in the equation
def cosine_similarity_calculator(document_vector, query_vector):
    dot_product = 0.0
    for i in range(len(document_vector)):
        dot_product += document_vector[i] * query_vector[i]

    return dot_product / (length_parameter_calculator.length_calculator(
        document_vector) * length_parameter_calculator.length_calculator(query_vector))
