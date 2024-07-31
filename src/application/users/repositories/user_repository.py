from src.adapter import CreateUserDto
from src.domain import User, UserRepository
from ..entities import UserEntity


class UserRepositoryImpl(UserRepository):

    @staticmethod
    def create_user(user: CreateUserDto) -> User:
        user_created = UserEntity.insert(user).on_conflict_do_nothing()
        print(user_created)
        return user_created

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserEntity.query.filter_by(user_id=user_id).first()
