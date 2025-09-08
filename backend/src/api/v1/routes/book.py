from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from src.core.components.v1.books.application.use_cases.book_search import (
    BookSearchUseCase,
)
from src.core.components.v1.books.infra.schemas.book import BookSearchPaginatedResponse
from src.core.di.containers import Container
from src.core.middlewares.models.base_response import BaseResponse
from src.core.utils.fastapi.get_responses import get_responses

book_router = APIRouter(prefix="/books", tags=["Books"])


@book_router.get("/search", responses=get_responses(BookSearchPaginatedResponse))
@inject
async def search_books(
    search_term: str = None,
    limit: Optional[int] = 25,
    offset: Optional[int] = 0,
    author: Optional[str] = None,
    publisher: Optional[str] = None,
    title: Optional[str] = None,
    book_search_use_case: BookSearchUseCase = Depends(
        Provide[Container.components.book.book_search_use_case]
    ),
):
    res = await book_search_use_case.execute(
        search_term=search_term,
        limit=limit,
        offset=offset,
        author=author,
        publisher=publisher,
        title=title,
    )

    return BaseResponse(message="Books successfully obtained", data=res)
