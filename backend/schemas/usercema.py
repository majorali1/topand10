from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

# this is required properties during user creation


class UserCreate(BaseModel):
    username: str = Field(..., min_length=5)
    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class ConfigDict:
        from_attributes = True
