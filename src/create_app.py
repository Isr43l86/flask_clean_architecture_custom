import os

from dotenv import load_dotenv
from flask import Flask

from .database import db
from .error_handler import setup_error_handler
from .infrastructure import UsersController, DocumentGeneratorController
from .logging import setup_logging

load_dotenv()


def create_app():
    app = Flask(__name__.split('.')[0])
    app = setup_logging(app)
    app = setup_error_handler(app)

    # Database initialization
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f"{os.getenv('DB_TYPE')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register controllers
    app.register_blueprint(UsersController)
    app.register_blueprint(DocumentGeneratorController)

    return app
