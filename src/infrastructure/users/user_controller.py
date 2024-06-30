from flask import Blueprint

from src.application import app_constants, UserService
from ..responses import create_response

UsersController = Blueprint(
    'users',
    __name__,
    url_prefix=f'/{app_constants.APP_CONTEXT}/{app_constants.APP_VERSION}/users'
)


@UsersController.route('/', methods=['GET'])
def index():
    return 'Hello World!'


@UsersController.route('/<user_id>', methods=['GET'])
def find_user_by_id(user_id):
    user_found = UserService.find_by_id(user_id)
    return create_response(user_found, 201)
