from datasource import Repository


def calculate_tfidf():
    repository = Repository()
    for req_word in repository.fetch_all_req_words():
        word = repository.fetch_word_by_id(req_word.word_id)
        if word is None:
            continue
        req_word.tfidf = req_word.tf * word.idf
        repository.update_req_word(req_word)


# main
if __name__ == '__main__':
    calculate_tfidf()
