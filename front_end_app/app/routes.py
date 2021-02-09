import requests
from flask import current_app as app
from flask import Flask, url_for, render_template, redirect, request
from app.forms import PredictionForm


def get_api_prediction(data, username, password):
    ''' Using HTTP Basic Authentication '''
    # api_endpoint = 'http://localhost:8000/api/v1.0'
    api_endpoint = 'http://api:8000/api/v1.0'

    credentials = (username, password)

    try:
        response = requests.get(url=api_endpoint, params=data, auth=credentials)
        response.raise_for_status()
        return response.json()['response']

    except requests.exceptions.HTTPError as errh:
        return {'Error': 'An Http Error occurred:' + repr(errh)}
    except requests.exceptions.ConnectionError as errc:
        return {'Error': 'An Error Connecting to the API occurred:' + repr(errc)}
    except requests.exceptions.Timeout as errt:
        return {'Error' : 'A Timeout Error occurred:' + repr(errt)}
    except requests.exceptions.RequestException as err:
        return {'Error' : 'An Unknown Error occurred' + repr(err)}


@app.route('/', methods=['GET'])
def home():
    form = PredictionForm()
    if form.validate_on_submit():
        return redirect(url_for('prediction'))
    return render_template('home.html', form=form, template='form-template')

@app.route('/prediction', methods=['GET'])
def prediction():

    sepal_length = request.args.get('sepal_length')
    sepal_width = request.args.get('sepal_width')
    petal_length = request.args.get('petal_length')
    petal_width = request.args.get('petal_width')

    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
        }

    ''' Sending GET request to ML api '''
    json_response = get_api_prediction(data, 'my_username', 'my_password')

    if json_response.get('predicted_species') != None:
        predicted_species = json_response.get('predicted_species')

        return render_template('prediction.html', species=predicted_species, template='success-template')
    elif '400 Client Error: BAD REQUEST for url' in json_response['Error']:
        # wrong data entry (strings instead of numbers)
        return redirect(url_for('wrong_data_type'))
    else:
        # can't connect to api server
        return redirect(url_for('bad_api_connection'))

@app.route('/wrong_data_type', methods=['GET'])
def wrong_data_type():
        return render_template('wrong_data_type.html', template='wrong_data_type-template')

@app.route('/bad_api_connection', methods=['GET'])
def bad_api_connection():
        return render_template('bad_api_connection.html', template='bad_api_connection-template')
