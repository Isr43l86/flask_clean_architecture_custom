from pydantic import BaseModel


class CreateUser(BaseModel):
    userId: int
    personId: str
    userName: str
