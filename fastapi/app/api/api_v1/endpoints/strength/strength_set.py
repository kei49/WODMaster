from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/strength_set/", response_model=List[schemas.strength.StrengthSet])
def read_strength_sets_with_user_id(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve strength_sets.
    """
    strength_sets = crud.strength_set.get_multi_with_user_id(db, current_user=current_user)
    return strength_sets


@router.post("/strength_set/", response_model=schemas.strength.StrengthSet)
def create_strength_set(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.strength.StrengthSetCreate
) -> Any:
    """
    Create a strength_set.
    """
    crud.sod.exist_check(db=db, id=obj_in.sod_id, name="sod")
    crud.strength_master.exist_check(db=db, id=obj_in.strength_master_id, name="strength master")
    strength_set = crud.strength_set.create(db, obj_in=obj_in)
    return strength_set


@router.put("/strength_set/{id}", response_model=schemas.strength.StrengthSet)
def update_strength_set(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: schemas.strength.StrengthSetUpdate,
) -> Any:
    """
    Update a strength_set.
    """
    strength_set = crud.strength_set.exist_check(db=db, id=id)
    strength_set = crud.strength_set.update(db=db, db_obj=strength_set, obj_in=obj_in)
    return strength_set


@router.delete("/strength_set/{id}", response_model=schemas.strength.StrengthSet)
def delete_strength_set(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a strength_set.
    """
    strength_set = crud.strength_set.exist_check(db=db, id=id)
    strength_set = crud.strength_set.remove(db=db, id=id)
    return strength_set