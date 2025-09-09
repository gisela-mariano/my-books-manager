from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.core.components.v1.books.application.use_cases.book_search import (
    BookSearchUseCase,
)
from src.core.components.v1.books.infra.schemas.book import BookSearchPaginatedResponse
from src.core.components.v1.books.utils.routes import get_book_search_parameters
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.get("/search", responses=get_responses(BookSearchPaginatedResponse))
@inject
async def search_books(
    params: Annotated[dict, Depends(get_book_search_parameters)],
    book_search_use_case: BookSearchUseCase = Depends(
        Provide[Container.components.book.book_search_use_case]
    ),
):
    res = await book_search_use_case.execute(**params)

    return BaseResponse(message="Books successfully obtained", data=res)
