from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings

router = APIRouter()


@router.get("/sod_score/", response_model=List[schemas.strength_score.SodScore])
def read_sod_scores_with_user_id(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: schemas.user.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve sod_scores.
    """
    sod_scores = crud.sod_score.get_multi_with_user_id(db, current_user=current_user)
    return sod_scores


@router.post("/sod_score/", response_model=schemas.strength_score.SodScore)
def create_sod_score(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: schemas.strength_score.SodScoreCreate
) -> Any:
    """
    Create a sod_score.
    """
    sod_score = crud.sod_score.create(db, obj_in=obj_in)
    return sod_score


@router.put("/sod_score/{id}", response_model=schemas.strength_score.SodScore)
def update_sod_score(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: schemas.strength_score.SodScoreUpdate,
) -> Any:
    """
    Update a sod_score.
    """
    sod_score = crud.sod_score.exist_check(db=db, id=id)
    sod_score = crud.sod_score.update(db=db, db_obj=sod_score, obj_in=obj_in)
    return sod_score


@router.delete("/sod_score/{id}", response_model=schemas.strength_score.SodScore)
def delete_sod_score(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete a sod_score.
    """
    sod_score = crud.sod_score.exist_check(db=db, id=id)
    sod_score = crud.sod_score.remove(db=db, id=id)
    return sod_score