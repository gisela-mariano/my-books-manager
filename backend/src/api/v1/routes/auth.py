from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.core.components.v1.auth.domain.auth_service import AuthService
from src.core.components.v1.auth.infra.schemas.auth import AuthLogin, Token
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/token", responses=get_responses(Token))
@inject
async def login_for_access_token(
    payload: AuthLogin,
    auth_service: AuthService = Depends(Provide[Container.components.auth.service]),
):
    res = await auth_service.authenticate_user(
        email=payload.email, password=payload.password
    )

    return BaseResponse(message="Token successfully obtained", data=res)
