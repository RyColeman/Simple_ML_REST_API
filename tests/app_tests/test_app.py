import json
import pytest
from flask import url_for

'''Instructions:

In the terminal window, run "$ pytest" in the same directory as this script.
'''

'''
In the pytest unit testing module, you configure variables, such as 'app' and 'client' as seen here, in a separate script called conftest.py
'''


def test_index(app, client):
    r = client.get('/')

    assert r.status_code == 200


def test_prediction_page(app, client):
    data = {
        'sepal_length': 1,
        'sepal_width': 1,
        'petal_length': 1,
        'petal_width': 1
        }

    r = client.get('/prediction')
    assert r.status_code == 302

    r_redirect = client.get('/prediction', query_string=data, follow_redirects=True)
    assert r_redirect.status_code == 200

def test_wrong_input_data_page(app, client):
    r = client.get('/wrong_data_type')

    assert r.status_code == 200

def test_bad_api_connection_page(app, client):
    r = client.get('/bad_api_connection')

    assert r.status_code == 200
