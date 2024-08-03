import logging

from flask_sqlalchemy import SQLAlchemy

from src.adapter import CreateUserDto
from src.domain import User, UserRepository
from ..entities import UserEntity

logger = logging.getLogger(__name__)


class UserRepositoryImpl(UserRepository):

    @staticmethod
    def create_user(db: SQLAlchemy, user: CreateUserDto) -> User:
        new_user = UserEntity(**user.model_dump())
        db.session.add(new_user)
        return new_user

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserEntity.query.filter_by(user_id=user_id).first()
