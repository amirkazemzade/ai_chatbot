# term_frequency : tf
# term : word
# document : sentence
def term_frequency(term: str, document: str):
    # normalized_document = document.lower().split()
    normalized_document = document.split(" ")
    # return normalized_document.count(term.lower()) / float(len(normalized_document))
    return normalized_document.count(term) / float(len(normalized_document))
