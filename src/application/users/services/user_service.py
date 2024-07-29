from src.domain import User, UserService
from ..repositories import UserRepositoryImpl


class UserServiceImpl(UserService):

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserRepositoryImpl.find_by_id(user_id)
