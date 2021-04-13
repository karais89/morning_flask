from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db = SQLAlchemy(app)

    @app.route("/")
    def hello():
        return "Hello, App!"

    return app