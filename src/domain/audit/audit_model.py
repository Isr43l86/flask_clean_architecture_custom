from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Status(str, Enum):
    active = '1'
    inactive = '0'


class AuditFields(BaseModel):
    status: Optional[str] = Status.active
    created_by_user: Optional[int] = None
    created_date: Optional[datetime] = None
    last_modified_by_user: Optional[int] = None
    last_modified_date: Optional[datetime] = None
    created_from_ip: Optional[str] = None
    updated_from_ip: Optional[str] = None
