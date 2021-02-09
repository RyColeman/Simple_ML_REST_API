'''Instructions:

1. Make sure the api is running. You can either navigate to the root directory and enter "$ docker-compose up" in terminal, or navigate to api.py and enter "$ python api.py".

2. In a separate terminal window, run "$ pytest" in the same directory as this script.

'''

import pytest
import requests

api_endpoint = 'http://localhost:8000/api/v1.0'

class TestAPI():
    def test_successful_json_response(self):
        data = {
            "sepal_length": 1,
            "sepal_width": 1,
            "petal_length": 1,
            "petal_width": 2
            }
        credentials = ('my_username', 'my_password')
        response = requests.get(url=api_endpoint, params=data, auth=credentials)

        assert response.status_code == 200
        assert response.json().get('response', 'Not a successful response') != 'Not a successful response'

    def test_wrong_basic_auth_credentials_response(self):
        data = {
            "sepal_length": 1,
            "sepal_width": 1,
            "petal_length": 1,
            "petal_width": 1
            }
        credentials = ('wrong_username', 'wrong_password')
        response = requests.get(url=api_endpoint, params=data, auth=credentials)

        assert response.json()['message'] == 'Unauthorized access'

    def test_wrong_input_data_response(self):
        data = {
            "sepal_length": 1,
            "sepal_width": 1,
            "petal_length": "This is not a float",
            "petal_width": 1
            }
        credentials = ('my_username', 'my_password')
        response = requests.get(url=api_endpoint, params=data, auth=credentials)

        assert response.json()['message']['petal_length'] == "Please provide petal_length data and make sure it is a 'float' type"
