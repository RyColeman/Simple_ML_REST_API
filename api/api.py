from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth
import pickle

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'my_username':
        return 'my_password'
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

class Predict(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('sepal_length', type=float,
            required=True,
            help="Please provide sepal_length data and make sure it is a 'float' type",
            location='args')
        self.reqparse.add_argument('sepal_width', type=float,
            required=True,
            help="Please provide sepal_width data and make sure it is a 'float' type",
            location='args')
        self.reqparse.add_argument('petal_length', type=float,
            required=True,
            help="Please provide petal_length data and make sure it is a 'float' type",
            location='args')
        self.reqparse.add_argument('petal_width', type=float,
            required=True,
            help="Please provide petal_width data and make sure it is a 'float' type",
            location='args')
        super().__init__()

    def get(self):
        args = self.reqparse.parse_args()
        sepal_length = args['sepal_length']
        sepal_width = args['sepal_width']
        petal_length = args['petal_length']
        petal_width = args['petal_width']

        data = [[sepal_length, sepal_width, petal_length, petal_width]]
        pred = model.predict(data)

        if pred == 0:
            species = 'Iris-Setosa'
        elif pred == 1:
            species = 'Iris-Versicolour'
        else:
            species = 'Iris-Virginica'

        response = {
            'predicted_species': species}

        return {'response': response}, 200


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(Predict, '/api/v1.0', endpoint='prediction')


if __name__ == '__main__':
    # Importing model from .pkl file:
    model = pickle.load(open('models/model.pkl', 'rb'))
    app.run(host="0.0.0.0", port=8000, debug=True)
