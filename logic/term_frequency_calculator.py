
# term_frequency : tf
# term : word
# document : sentence
def term_frequency(term, document):
    normalized_document = document.lower().split()
    return normalized_document.count(term.lower()) / float(len(normalized_document))

