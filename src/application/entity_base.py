from datetime import datetime

import pytz

from src.database import db
from src.domain import Status
from .constants import app_constants


class AuditMixin:
    status = db.Column(db.String(1), default=Status.active)
    created_by_user = db.Column(db.Integer)
    created_date = db.Column(db.TIMESTAMP, default=datetime.now(pytz.timezone(app_constants.APP_TIMEZONE)))
    last_modified_by_user = db.Column(db.Integer)
    last_modified_date = db.Column(db.TIMESTAMP)
    created_from_ip = db.Column(db.String(64), default=app_constants.DEFAULT_IP_ADDRESS)
    updated_from_ip = db.Column(db.String(64))
