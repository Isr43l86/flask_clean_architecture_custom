from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AuditFields(BaseModel):
    status: Optional[bool] = True
    created_by_user: Optional[int] = None
    created_date: Optional[datetime] = None
    last_modified_by_user: Optional[int] = None
    last_modified_date: Optional[datetime] = None
    created_from_ip: Optional[str] = None
    updated_from_ip: Optional[str] = None
