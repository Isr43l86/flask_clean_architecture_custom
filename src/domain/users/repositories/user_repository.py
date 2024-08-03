from abc import ABC, abstractmethod

from flask_sqlalchemy import SQLAlchemy

from src.adapter import CreateUserDto
from ..models import User


class UserRepository(ABC):

    @staticmethod
    @abstractmethod
    def create_user(db: SQLAlchemy, user: CreateUserDto) -> User:
        pass

    @staticmethod
    @abstractmethod
    def find_by_id(db: SQLAlchemy, user_id: str) -> User:
        pass
