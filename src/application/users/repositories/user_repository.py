from src.domain import User, UserRepository
from ..entities import UserEntity


class UserRepositoryImpl(UserRepository):

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserEntity.query.filter_by(user_id=user_id).first()
