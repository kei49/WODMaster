from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/user_sod/", response_model=List[schemas.strength_score.UserSod])
def read_user_sods_with_user_id(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.user.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve user_sods.
    """
    user_sods = crud.user_sod.get_multi_with_user_id(db, current_user=current_user)
    return user_sods


@router.post("/user_sod/", response_model=schemas.strength_score.UserSod)
def create_user_sod(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.strength_score.UserSodCreate
) -> Any:
    """
    Create a user_sod.
    """
    user_sod = crud.user_sod.create(db, obj_in=obj_in)
    return user_sod


@router.put("/user_sod/{id}", response_model=schemas.strength_score.UserSod)
def update_user_sod(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: schemas.strength_score.UserSodUpdate,
) -> Any:
    """
    Update a user_sod.
    """
    user_sod = crud.user_sod.exist_check(db=db, id=id)
    user_sod = crud.user_sod.update(db=db, db_obj=user_sod, obj_in=obj_in)
    return user_sod


@router.delete("/user_sod/{id}", response_model=schemas.strength_score.UserSod)
def delete_user_sod(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a user_sod.
    """
    user_sod = crud.user_sod.exist_check(db=db, id=id)
    user_sod = crud.user_sod.remove(db=db, id=id)
    return user_sod