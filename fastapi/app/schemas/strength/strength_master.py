from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class StrengthMasterBase(BaseModel):
    name: str = None


# Properties to receive via API on creation
class StrengthMasterCreate(StrengthMasterBase):
    pass


# Properties to receive via API on update
class StrengthMasterUpdate(StrengthMasterBase):
    pass


class StrengthMasterInDBBase(StrengthMasterBase):
    id: Optional[int] = None
    pass

    class Config:
        orm_mode = True


# Additional properties to return via API
class StrengthMaster(StrengthMasterInDBBase):
    pass