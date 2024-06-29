from abc import ABC
from typing import Callable

from src.domain import User
from ..entities import UserEntity


class UserRepository(ABC):
    base_class: Callable

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserEntity.query.filter_by(user_id=user_id).one_or_none()
