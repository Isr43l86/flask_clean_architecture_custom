import logging

from flask_sqlalchemy import SQLAlchemy

from src.adapter import CreateUserDto, UpdateUserDto
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
    def find_by_id(db: SQLAlchemy, user_id: str) -> User | None:
        user_found = db.session.execute(db.Select(UserEntity).where(UserEntity.user_id == user_id)).scalar()
        if user_found:
            return user_found

        raise CustomError(error_messages.USER_NOT_FOUND, 404)

    @staticmethod
    def update_user(db: SQLAlchemy, user_id: str, user: UpdateUserDto) -> User:
        user_found = UserRepositoryImpl.find_by_id(db, user_id)
        if user_found:
            update_data = user.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                if hasattr(user_found, key):
                    setattr(user_found, key, value)
                else:
                    attribute_error = f"{key} is not a valid attribute of UserEntity"
                    logger.error(attribute_error)
                    raise AttributeError(attribute_error)

            return user_found

        raise CustomError(error_messages.USER_NOT_FOUND, 404)
