''' Starting with python 3.3, you cannot reference parent directories when importing modules. The solution is a bit hacky, but you can add in additional PYTHONPATHs through sys.path to create paths to relevant files for module imports
'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(parentdir)
appdir = rootdir + '/front_end_app'
sys.path.append(appdir)
sys.path.append(rootdir)

import pytest

from front_end_app import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    return app.test_client()
