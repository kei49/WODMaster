from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class SodScoreBase(BaseModel):
    user_id: int = None
    sod_id: int = None
    comment: str = True
    

# Properties to receive via API on creation
class SodScoreCreate(SodScoreBase):
    pass


# Properties to receive via API on update
class SodScoreUpdate(SodScoreBase):
    pass

class SodScoreInDBBase(SodScoreBase):
    id: Optional[int] = None
    created: datetime = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SodScore(SodScoreInDBBase):
    pass