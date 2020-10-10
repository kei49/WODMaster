from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class SodBase(BaseModel):
    creator_id: int = None
    name: str = None
    public: bool = True


# Properties to receive via API on creation
class SodCreate(SodBase):
    pass


# Properties to receive via API on update
class SodUpdate(SodBase):
    pass

class SodInDBBase(SodBase):
    id: Optional[int] = None
    created: datetime = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Sod(SodInDBBase):
    pass