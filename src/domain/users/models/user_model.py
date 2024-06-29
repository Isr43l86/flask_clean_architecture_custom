from src.domain.audit.audit_model import AuditFields


class User(AuditFields):
    userId: int
    personId: str
    userName: str
