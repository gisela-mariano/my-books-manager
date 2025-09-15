from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends
from src.core.components.v1.users.application.use_cases.user_create_use_case import (
    UserCreateUseCase,
)
from src.core.components.v1.users.application.use_cases.user_find_by_id_use_case import (
    UserFindByIdUseCase,
)
from src.core.components.v1.users.application.use_cases.user_update_use_case import (
    UserUpdateUseCase,
)
from src.core.components.v1.users.infra.schemas.user import (
    UserCreate,
    UserDbResponse,
    UserUpdate,
)
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

prefix = "/users"
tags = ["Users"]

user_router = APIRouter(prefix=prefix, tags=tags)
user_public_router = APIRouter(prefix=prefix, tags=tags)


@user_public_router.post("", responses=get_responses(UserDbResponse))
@inject
async def create_user(
    payload: UserCreate = Body(...),
    user_create_use_case: UserCreateUseCase = Depends(
        Provide[Container.components.user.user_create_use_case]
    ),
):
    res = await user_create_use_case.execute(payload)

    return BaseResponse(message="User successfully created", data=res)


@user_router.get("/{user_id}", responses=get_responses(UserDbResponse))
@inject
async def find_user_by_id(
    user_id: str,
    user_find_by_id_use_case: UserFindByIdUseCase = Depends(
        Provide[Container.components.user.user_find_by_id_use_case]
    ),
):
    res = await user_find_by_id_use_case.execute(user_id)

    return BaseResponse(message="User successfully obtained", data=res)


@user_router.get("/email/{user_email}", responses=get_responses(UserDbResponse))
@inject
async def find_user_by_email(
    user_email: str,
    user_find_by_email_use_case: UserFindByIdUseCase = Depends(
        Provide[Container.components.user.user_find_by_email_use_case]
    ),
):
    res = await user_find_by_email_use_case.execute(user_email)

    return BaseResponse(message="User successfully obtained", data=res)


@user_router.get("/username/{username}", responses=get_responses(UserDbResponse))
@inject
async def find_user_by_username(
    username: str,
    user_find_by_username_use_case: UserFindByIdUseCase = Depends(
        Provide[Container.components.user.user_find_by_username_use_case]
    ),
):
    res = await user_find_by_username_use_case.execute(username)

    return BaseResponse(message="User successfully obtained", data=res)


@user_router.patch("/{user_id}", responses=get_responses(UserDbResponse))
@inject
async def update_user(
    user_id: str,
    payload: UserUpdate = Body(...),
    user_update_use_case: UserUpdateUseCase = Depends(
        Provide[Container.components.user.user_update_use_case]
    ),
):
    res = await user_update_use_case.execute(id=user_id, user=payload)

    return BaseResponse(message="User successfully updated", data=res)


@user_router.delete("/{user_id}", responses=get_responses(None))
@inject
async def delete_user(
    user_id: str,
    user_deactivate_use_case: UserFindByIdUseCase = Depends(
        Provide[Container.components.user.user_deactivate_use_case]
    ),
):
    await user_deactivate_use_case.execute(id=user_id)

    return BaseResponse(message="User successfully deleted")
