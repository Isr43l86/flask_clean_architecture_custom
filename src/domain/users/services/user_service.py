from abc import ABC, abstractmethod

from src.adapter import CreateUserDto, UpdateUserDto
from ..models import User


class UserService(ABC):

    @staticmethod
    @abstractmethod
    def create_user(user: CreateUserDto) -> User:
        pass

    @staticmethod
    @abstractmethod
    def find_by_id(user_id: str) -> User:
        pass

    @staticmethod
    @abstractmethod
    def update_user(user_id: str, user: UpdateUserDto) -> User:
        pass
