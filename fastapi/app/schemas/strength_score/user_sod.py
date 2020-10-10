from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class UserSodBase(BaseModel):
    user_sod_id: int = None
    location: int = None
    weight: float = True


# Properties to receive via API on creation
class UserSodCreate(UserSodBase):
    pass


# Properties to receive via API on update
class UserSodUpdate(UserSodBase):
    pass

class UserSodInDBBase(UserSodBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserSod(UserSodInDBBase):
    pass