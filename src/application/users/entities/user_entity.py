from src.application import AuditMixin
from src.database import db
from ...constants import database_constants


class UserEntity(AuditMixin, db.Model):
    __tablename__ = f'{database_constants.KSECURITY_PREFIX}_user'
    __table_args__ = {"schema": database_constants.KSECURITY_SCHEMA}
    user_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    username = db.Column(db.String)
