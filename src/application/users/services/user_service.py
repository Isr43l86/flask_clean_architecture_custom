from src.adapter import CreateUserDto
from src.domain import User, UserService
from ..repositories import UserRepositoryImpl


class UserServiceImpl(UserService):

    @staticmethod
    def create_user(user: CreateUserDto) -> User:
        return UserRepositoryImpl.create_user(user)

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserRepositoryImpl.find_by_id(user_id)
