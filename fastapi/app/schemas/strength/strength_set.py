from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class StrengthSetBase(BaseModel):
    sod_id: int = None
    strength_master_id: int = None
    location: int = None
    time: float = None
    reps: int = None


# Properties to receive via API on creation
class StrengthSetCreate(StrengthSetBase):
    pass


# Properties to receive via API on update
class StrengthSetUpdate(StrengthSetBase):
    pass


class StrengthSetInDBBase(StrengthSetBase):
    id: Optional[int] = None
    pass

    class Config:
        orm_mode = True


# Additional properties to return via API
class StrengthSet(StrengthSetInDBBase):
    pass