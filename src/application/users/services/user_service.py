import logging

from src.adapter import CreateUserDto
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
    def find_by_id(user_id: int) -> User | None:
        return UserRepositoryImpl.find_by_id(user_id)
