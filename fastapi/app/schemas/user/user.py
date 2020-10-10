from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    first_name: str = None
    last_name: str = None
    email: Optional[EmailStr] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    pass


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: Optional[int] = None
    pass

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str