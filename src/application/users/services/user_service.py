from abc import ABC
from typing import Callable

from src.domain import User
from ..repositories import UserRepository


class UserService(ABC):
    base_class: Callable

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserRepository.find_by_id(user_id)
