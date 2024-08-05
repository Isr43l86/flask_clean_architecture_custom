from flask import Blueprint

from src.adapter import CreateUserDto, UpdateUserDto
from src.application import app_constants, UserServiceImpl
from ..custom_decorators import validate_body
from ..responses import create_response

UsersController = Blueprint(
    'users',
    __name__,
    url_prefix=f'/{app_constants.APP_CONTEXT}/{app_constants.APP_VERSION}/users'
)


@UsersController.route('/<user_id>', methods=['GET'])
def find_user_by_id(user_id: str):
    user_found = UserServiceImpl.find_by_id(user_id)
    return create_response(user_found, 201)


@UsersController.route('', methods=['POST'])
@validate_body(CreateUserDto)
def create_user(user: CreateUserDto):
    user_created = UserServiceImpl.create_user(user)
    return create_response(user_created, 201)


@UsersController.route('/<user_id>', methods=['PUT'])
@validate_body(UpdateUserDto)
def update_user(user: UpdateUserDto, user_id: str):
    user_updated = UserServiceImpl.update_user(user_id, user)
    return create_response(user_updated, 200)


@UsersController.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id: str):
    UserServiceImpl.delete_user(user_id)
    return create_response(app_constants.USER_SUCCESS_DELETING, 200)
