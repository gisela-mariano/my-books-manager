from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends
from src.core.components.v1.users.application.use_cases.user_creation_use_case import (
    UserCreationUseCase,
)
from src.core.components.v1.users.infra.schemas.user import UserCreate, UserDbResponse
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("", responses=get_responses(UserDbResponse))
@inject
async def create_user(
    payload: UserCreate = Body(...),
    user_creation_use_case: UserCreationUseCase = Depends(
        Provide[Container.components.user.user_creation_use_case]
    ),
):
    res = await user_creation_use_case.execute(payload)

    return BaseResponse(message="User successfully created", data=res)
