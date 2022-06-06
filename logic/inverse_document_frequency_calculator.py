import math

from datasource.models import RequestModel


# inverse_document_frequency : idf
# term : word
def inverse_document_frequency(term: str, list_of_all_document: list[RequestModel]):
    num_of_document_with_this_term = 0
    for doc in list_of_all_document:
        # if term.lower() in doc.req.lower().split():
        if term in doc.req.split(" "):
            num_of_document_with_this_term += 1

    if num_of_document_with_this_term > 0:
        return 1.0 + math.log((float(len(list_of_all_document)) / num_of_document_with_this_term), 2)
    else:
        return 1.0
