# a function to update word table by splitting request table sentences
from datasource import Repository
from datasource.models import WordModel, ReqWordModel
from logic import term_frequency_calculator


def update_word_by_request():
    repository = Repository()
    # get all requests
    requests = repository.fetch_all_requests()
    # split requests sentences
    for request in requests:
        # get req
        req = request.req
        # split req sentences
        sentences = req.split(" ")
        for sentence in sentences:
            # get word
            word = repository.find_word_by_string(sentence)
            # if word is not found, create new word
            if word is None:
                word = WordModel(word=sentence)
                word.id = repository.insert_word(word)
            # get req_word
            req_word = repository.fetch_req_word_by_req_id_word_id(word.id, request.id)
            # if req_word is not found, create new req_word
            if req_word is None:
                req_word = ReqWordModel(req_id=request.id, word_id=word.id)
                req_word.id = repository.insert_req_word(req_word)
            # update req_word
            tf = request.req.count(word.word) / len(request.req)
            # tf = term_frequency_calculator.term_frequency(word.word, request.req)
            req_word.tf = tf
            repository.update_req_word(req_word)


if __name__ == '__main__':
    update_word_by_request()
