from abc import ABC, abstractmethod

from ..models import User


class UserRepository(ABC):
    @staticmethod
    @abstractmethod
    def find_by_id(user_id: str) -> User:
        pass
