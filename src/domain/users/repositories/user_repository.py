from abc import ABC, abstractmethod

from src.adapter import CreateUserDto
from ..models import User


class UserRepository(ABC):

    @staticmethod
    @abstractmethod
    def create_user(user: CreateUserDto) -> User:
        pass

    @staticmethod
    @abstractmethod
    def find_by_id(user_id: str) -> User:
        pass
