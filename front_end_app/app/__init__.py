"""Initialize app."""
from flask import Flask
from config import Config


def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    with app.app_context():
        from . import routes

        return app
