import logging

from src.adapter import CreateUserDto, UpdateUserDto
from src.database import db
from src.domain import User, UserService
from src.exceptions import CustomError
from ..entities import UserEntity
from ..repositories import UserRepositoryImpl
from ...constants import error_messages
from ...utils import convert_entity_to_model

logger = logging.getLogger(__name__)


class UserServiceImpl(UserService):

    @staticmethod
    def create_user(user: CreateUserDto) -> User:
        user_created = UserRepositoryImpl.create_user(db, user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(error_messages.USER_ERROR_CREATING)
            raise CustomError(error_messages.USER_ERROR_CREATING)

        return convert_entity_to_model(UserEntity, User, user_created)

    @staticmethod
    def find_by_id(user_id: str) -> User | None:
        return UserRepositoryImpl.find_by_id(db, user_id)

    @staticmethod
    def update_user(user_id: str, user: UpdateUserDto) -> User:
        user_updated = UserRepositoryImpl.update_user(db, user_id, user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(error_messages.USER_ERROR_UPDATING)
            raise CustomError(error_messages.USER_ERROR_UPDATING)

        return convert_entity_to_model(UserEntity, User, user_updated)

    @staticmethod
    def delete_user(user_id: str) -> None:
        UserRepositoryImpl.delete_user(db, user_id)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(error_messages.USER_ERROR_DELETING)
            raise CustomError(error_messages.USER_ERROR_DELETING)

        return None
