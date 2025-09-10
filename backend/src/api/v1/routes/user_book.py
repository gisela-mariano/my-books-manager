from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, Request
from src.core.components.v1.books.infra.schemas.book import BookSearchPaginatedResponse
from src.core.components.v1.user_books.application.use_cases.user_book_create_use_case import (
    UserBookCreateUseCase,
)
from src.core.components.v1.user_books.infra.schemas.user_book import UserBookCreate
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

user_book_router = APIRouter(prefix="/user-books", tags=["User Books"])


@user_book_router.post("", responses=get_responses(BookSearchPaginatedResponse))
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
