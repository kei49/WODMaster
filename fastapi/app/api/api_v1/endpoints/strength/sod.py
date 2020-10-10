from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/sod/", response_model=List[schemas.strength.Sod])
def read_sods_with_user_id(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve sods.
    """
    sods = crud.sod.get_multi(db, skip=skip, limit=limit)
    return sods


@router.post("/sod/", response_model=schemas.strength.Sod)
def create_sod(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.strength.SodCreate
) -> Any:
    """
    Create a sod.
    """
    sod = crud.sod.create_with_time(db, obj_in=obj_in)
    return sod


@router.put("/sod/{id}", response_model=schemas.strength.Sod)
def update_sod(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: schemas.strength.SodUpdate,
) -> Any:
    """
    Update a sod.
    """
    sod = crud.sod.exist_check(db=db, id=id)
    sod = crud.sod.update(db=db, db_obj=sod, obj_in=obj_in)
    return sod


@router.delete("/sod/{id}", response_model=schemas.strength.Sod)
def delete_sod(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a sod.
    """
    sod = crud.sod.exist_check(db=db, id=id)
    sod = crud.sod.remove(db=db, id=id)
    return sod