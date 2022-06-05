from datasource import Repository
from datasource.models import WordModel, ReqWordModel
import logic.logic


def tf_calculator():
    # repository instance
    repo = Repository()

    # get list of all documents
    docs = repo.fetch_all_requests()

    for doc in docs:
        # get document from doc (it is a Request Model)
        document = doc.req

        words = document.split()
        for word in words:
            # get word model (related to this word)
            word_model = repo.find_word_by_string(word)
            # if word is not found, create new word
            if word_model is None:
                word_model = WordModel(word=word)
                word_model.id = repo.insert_word(word_model)
            # get req_word
            req_word = repo.fetch_req_word_by_req_id_word_id(word_model.id, doc.id)

            # if req_word is not found, create new req_word
            if req_word is None:
                req_word = ReqWordModel(req_id=doc.id, word_id=word_model.id)
                req_word.id = repo.insert_req_word(req_word)

            tf_value = logic.term_frequency(word_model.word, doc.req)
            req_word.tf = tf_value
            repo.update_req_word(req_word)


def idf_calculator():
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
        idf_value = logic.inverse_document_frequency(word_model.word, docs_list)
        word_model.idf = idf_value

        repo.update_word(word_model)


def length_calculator():
    # repository instance
    repo = Repository()

