from pydantic import BaseModel


class CreateUserDto(BaseModel):
    personId: str
    userName: str
