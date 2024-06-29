from dotenv import load_dotenv
from flask import Flask

from .error_handler import setup_error_handler
from .infrastructure import UsersController
from .logging import setup_logging

load_dotenv()


def create_app():
    app = Flask(__name__.split('.')[0])
    app = setup_logging(app)
    app = setup_error_handler(app)

    # Register controllers
    app.register_blueprint(UsersController)

    return app
