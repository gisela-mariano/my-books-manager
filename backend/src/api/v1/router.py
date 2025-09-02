from fastapi import APIRouter
from src.api.v1.routes.user import user_router

routes = APIRouter(prefix="/v1")

routes.include_router(user_router)
