from sqlalchemy import Column, Integer, String

from src.application import AuditMixin
from src.database import Base
from ...constants import database_constants


class UserEntity(AuditMixin, Base):
    __tablename__ = f'{database_constants.KSECURITY_PREFIX}_user'
    __table_args__ = {"schema": database_constants.KSECURITY_SCHEMA}
    user_id = Column(Integer, primary_key=True)
    person_id = Column(Integer)
    username = Column(String)
