from datasource import Repository
from logic import inverse_document_frequency_calculator


# calculate idf that is in word table
def update_word():
    # repository instance
    repo = Repository()

    # get list of all words
    words_list = repo.fetch_all_words()

    # get list of all document (request)
    docs_list = repo.fetch_all_requests()

    # get number of all document (requests)
    # number_of_all_words = repo.count_words()

    for word_model in words_list:
        # get idf_value from logic's function
        idf_value = inverse_document_frequency_calculator.inverse_document_frequency(word_model.word, docs_list)
        word_model.idf = idf_value

        repo.update_word(word_model)


if __name__ == "__main__":
    update_word()
