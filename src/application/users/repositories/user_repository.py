import logging

from flask_sqlalchemy import SQLAlchemy

from src.adapter import CreateUserDto
from src.domain import User, UserRepository
from src.exceptions import CustomError
from ..entities import UserEntity
from ...constants import error_messages

logger = logging.getLogger(__name__)


class UserRepositoryImpl(UserRepository):

    @staticmethod
    def create_user(db: SQLAlchemy, user: CreateUserDto) -> User:
        new_user = UserEntity(user)
        db.session.add(new_user)
        return new_user

    @staticmethod
    def find_by_id(db: SQLAlchemy, user_id: int) -> User | None:
        user_found = db.session.execute(db.Select(UserEntity).where(UserEntity.user_id == user_id)).scalar()
        if user_found:
            return user_found

        raise CustomError(error_messages.USER_NOT_FOUND, 404)
