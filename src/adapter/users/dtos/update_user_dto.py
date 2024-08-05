from pydantic import BaseModel


class UpdateUserDto(BaseModel):
    username: str

    class Config:
        from_attributes = True
