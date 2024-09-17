
from pydantic import EmailStr,BaseModel,Field

#this is required properties during user creation

class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=4)