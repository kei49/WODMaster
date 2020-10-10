from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

#from app.core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.strength_score import SodScore, UserSod
from schemas.strength_score.sod_score import SodScoreCreate, SodScoreUpdate
from schemas.strength_score.user_sod import UserSodCreate, UserSodUpdate


class CRUDSodScore(CRUDBase[SodScore, SodScoreCreate, SodScoreUpdate]):
    pass


class CRUDUserSod(CRUDBase[UserSod, UserSodCreate, UserSodUpdate]):
    pass


sod_score = CRUDSodScore(SodScore)
user_sod = CRUDUserSod(UserSod)