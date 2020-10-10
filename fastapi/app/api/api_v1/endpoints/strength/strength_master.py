from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/strength_master/", response_model=List[schemas.strength.StrengthMaster])
def read_strength_masters_with_user_id(
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve strength_masters.
    """
    strength_masters = crud.strength_master.get_multi(db)
    return strength_masters


@router.post("/strength_master/", response_model=schemas.strength.StrengthMaster)
def create_strength_master(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.strength.StrengthMasterCreate
) -> Any:
    """
    Create a strength_master.
    """
    strength_master = crud.strength_master.create(db, obj_in=obj_in)
    return strength_master


@router.put("/strength_master/{id}", response_model=schemas.strength.StrengthMaster)
def update_strength_master(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: schemas.strength.StrengthMasterUpdate,
) -> Any:
    """
    Update a strength_master.
    """
    strength_master = crud.strength_master.exist_check(db=db, id=id)
    strength_master = crud.strength_master.update(db=db, db_obj=strength_master, obj_in=obj_in)
    return strength_master


@router.delete("/strength_master/{id}", response_model=schemas.strength.StrengthMaster)
def delete_strength_master(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a strength_master.
    """
    strength_master = crud.strength_master.exist_check(db=db, id=id)
    strength_master = crud.strength_master.remove(db=db, id=id)
    return strength_master