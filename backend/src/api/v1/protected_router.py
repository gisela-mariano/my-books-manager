from fastapi import APIRouter, Depends
from src.api.v1.routes.user import user_router
from src.core.utils.auth.auth_bearer import JWTBearer

routes = APIRouter(prefix="/v1", dependencies=[Depends(JWTBearer())])

routes.include_router(user_router)
