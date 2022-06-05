import unittest

from datasource.provider import Provider


# test provider.py
class TestProvider(unittest.TestCase):
    # test count words function
    def test_count_words(self):
        provider = Provider()
        self.assertEqual(provider.count_words(), 4)

    # test count requests function
    def test_count_requests(self):
        provider = Provider()
        self.assertEqual(provider.count_requests(), 112)

    # test get_last_request function
    def test_get_last_request(self):
        provider = Provider()
        self.assertEqual(provider.get_last_request(), provider.fetch_request_by_id(224))

    # test fetch_word_by_id function
    def test_fetch_word_by_id(self):
        provider = Provider()
        print(provider.fetch_word_by_id(1))

    # test get_last_word function
    def test_get_last_word(self):
        provider = Provider()
        self.assertEqual(provider.get_last_word(), provider.fetch_word_by_id(4))

    # test find_word_by_string function
    def test_find_word_by_string(self):
        provider = Provider()
        self.assertEqual(provider.find_word_by_string("test"), provider.fetch_word_by_id(1))


# test repository.py
class TestRepository(unittest.TestCase):
    # test fetch_word_by_id function
    def test_fetch_word_by_id(self):
        provider = Provider()
        self.assertEqual(provider.fetch_word_by_id(1), provider.fetch_word_by_id(1))
