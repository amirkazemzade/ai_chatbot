from datasource import Repository
from logic import length_parameter_calculator


# update request table after calculating length for each req
def update_request():
    # repository instance
    repo = Repository()

    # get list of all requests
    documents = repo.fetch_all_requests()

    for document in documents:
        # get list of all req_word model that have same req_id with this document
        req_word_model = repo.fetch_req_word_by_req_id(document.id)

        # calculating length value using logic's function
        length_value = length_parameter_calculator.length_calculator(req_word_model)

        # if document.length is None:
        document.length = length_value
        repo.update_request(document)


if __name__ == "__main__":
    update_request()
