from typing import List, Optional, Union

from pydantic import Field
from src.core.utils.models.base import BaseConfig, BaseInDb


class Book(BaseConfig):
    title: str = Field(max_length=255)
    subtitle: Optional[str] = Field(default=None, max_length=500)
    description: Optional[str] = Field(default=None)
    cover_url: Optional[str] = None
    isbn_10: Optional[str] = Field(default=None, min_length=10, max_length=10)
    isbn_13: Optional[str] = Field(default=None, min_length=13, max_length=13)
    page_count: Optional[int] = None
    published_date: Optional[str] = None


class BookDb(Book, BaseInDb):
    created_at: Optional[str] = Field(default=None)


class BookSearchPaginatedResponse(BaseConfig):
    books: Union[List[BookDb], List[Book]]
    total: int
