from fastapi import APIRouter

from api.api_v1.endpoints.user import login
from api.api_v1.endpoints.user import user
from api.api_v1.endpoints.strength import sod, strength_master, strength_set
from api.api_v1.endpoints.strength_score import sod_score, user_sod


api_router = APIRouter()
#api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])

api_router.include_router(sod.router, prefix="/strengths", tags=["strength/sods"])
api_router.include_router(strength_master.router, prefix="/strengths", tags=["strength/strength_masters"])
api_router.include_router(strength_set.router, prefix="/strengths", tags=["strength/strength_sets"])

api_router.include_router(sod_score.router, prefix="/strength_scores", tags=["strength_score/sod_scores"])
api_router.include_router(user_sod.router, prefix="/strength_scores", tags=["strength_score/user_sods"])
