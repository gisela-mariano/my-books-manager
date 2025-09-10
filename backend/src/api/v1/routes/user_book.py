from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, Request
from src.core.components.v1.user_books.application.use_cases.user_book_create_use_case import (
    UserBookCreateUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_get_by_id_use_case import (
    UserBookGetByIdUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_get_user_books import (
    UserBookGetUserBooksUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_update_use_case import (
    UserBookUpdateUseCase,
)
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookCreate,
    UserBookJoinBook,
    UserBooksJoinBookPaginatedResponse,
    UserBookUpdate,
)
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses
from src.core.utils.routes.get_pagination_parameters import get_pagination_parameters

user_book_router = APIRouter(prefix="/user-books", tags=["User Books"])


@user_book_router.post("", responses=get_responses(UserBookJoinBook))
@inject
async def create_book(
    request: Request,
    payload: UserBookCreate = Body(...),
    user_book_create_use_case: UserBookCreateUseCase = Depends(
        Provide[Container.components.user_book.user_book_create_use_case]
    ),
):
    user_id = request.state.user.get("id")

    res = await user_book_create_use_case.execute(payload=payload, user_id=user_id)

    return BaseResponse(message="Book successfully created", data=res)


@user_book_router.get("", responses=get_responses(UserBooksJoinBookPaginatedResponse))
@inject
async def get_user_books(
    request: Request,
    params: Annotated[dict, Depends(get_pagination_parameters)],
    user_book_get_user_books_use_case: UserBookGetUserBooksUseCase = Depends(
        Provide[Container.components.user_book.user_book_get_user_books_use_case]
    ),
):
    user_id = request.state.user.get("id")

    res = await user_book_get_user_books_use_case.execute(user_id=user_id, **params)

    return BaseResponse(message="Books successfully obtained", data=res)


@user_book_router.get("/{user_book_id}", responses=get_responses(UserBookJoinBook))
@inject
async def get_user_book_by_id(
    user_book_id: str,
    user_book_get_by_id_use_case: UserBookGetByIdUseCase = Depends(
        Provide[Container.components.user_book.user_book_get_by_id_use_case]
    ),
):
    res = await user_book_get_by_id_use_case.execute(id=user_book_id)

    return BaseResponse(message="Book successfully obtained", data=res)


@user_book_router.patch("/{user_book_id}", responses=get_responses(UserBookJoinBook))
@inject
async def update_user_book(
    user_book_id: str,
    payload: UserBookUpdate = Body(...),
    user_book_update_use_case: UserBookUpdateUseCase = Depends(
        Provide[Container.components.user_book.user_book_update_use_case]
    ),
):
    res = await user_book_update_use_case.execute(id=user_book_id, payload=payload)

    return BaseResponse(message="User Book successfully updated", data=res)
