from ...audit import AuditFields


class User(AuditFields):
    user_id: int
    person_id: int
    username: str

    class Config:
        from_attributes = True
