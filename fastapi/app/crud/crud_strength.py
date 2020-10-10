from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

#from app.core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.strength import Sod, StrengthMaster, StrengthSet
from schemas.strength.sod import SodCreate, SodUpdate
from schemas.strength.strength_master import StrengthMasterCreate, StrengthMasterUpdate
from schemas.strength.strength_set import StrengthSetCreate, StrengthSetUpdate


class CRUDSod(CRUDBase[Sod, SodCreate, SodUpdate]):
    pass


class CRUDStrengthMaster(CRUDBase[StrengthMaster, StrengthMasterCreate, StrengthMasterUpdate]):
    pass


class CRUDStrengthSet(CRUDBase[StrengthSet, StrengthSetCreate, StrengthSetUpdate]):
    pass


sod = CRUDSod(Sod)
strength_master = CRUDStrengthMaster(StrengthMaster)
strength_set = CRUDStrengthSet(StrengthSet)