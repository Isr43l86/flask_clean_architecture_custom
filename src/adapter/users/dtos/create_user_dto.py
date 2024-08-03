from pydantic import BaseModel


class CreateUserDto(BaseModel):
    person_id: str
    username: str

    class Config:
        from_attributes = True
