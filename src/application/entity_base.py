from datetime import datetime

import pytz
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP

from .constants import app_constants


class AuditMixin(object):
    status = Column(Boolean, default=True)
    created_by_user = Column(Integer)
    created_date = Column(TIMESTAMP, default=datetime.now(pytz.timezone(app_constants.APP_TIMEZONE)))
    last_modified_by_user = Column(Integer)
    last_modified_date = Column(TIMESTAMP)
    created_from_ip = Column(String, default=app_constants.DEFAULT_IP_ADDRESS)
    updated_from_ip = Column(String)
