from fastapi import APIRouter, Depends
from src.api.v1.routes.book import book_router
from src.api.v1.routes.user import user_router
from src.api.v1.routes.user_book import user_book_router
from src.core.utils.auth.auth_bearer import JWTBearer

routes = APIRouter(prefix="/v1", dependencies=[Depends(JWTBearer())])

routes.include_router(user_router)
routes.include_router(book_router)
routes.include_router(user_book_router)
