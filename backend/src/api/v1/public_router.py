from fastapi import APIRouter, Depends
from src.api.v1.routes.auth import auth_router
from src.api.v1.routes.user import user_public_router

routes = APIRouter(prefix="/v1")

routes.include_router(user_public_router)
routes.include_router(auth_router)
