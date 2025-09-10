from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import Field, field_serializer, field_validator
from src.core.components.v1.books.infra.schemas.book import Book
from src.core.utils.date import format_date_string_to_isoformat
from src.core.utils.models.base import BaseConfig, BaseInDb, exclude_fields


class UserBookReadingStatus(Enum):
    TO_READ = "to-read"
    READING = "reading"
    READ = "read"


class UserBook(BaseConfig):
    user_id: str
    book_id: str
    reading_status: Optional[UserBookReadingStatus] = None
    rating_star: Optional[int] = Field(default=None, ge=0, le=5)
    reading_start_date: Optional[str] = None
    reading_end_date: Optional[str] = None


class UserBookDb(UserBook, BaseInDb):
    pass


class UserBookJoinBook(UserBookDb):
    book: Book


@exclude_fields("user_id", "book_id")
class UserBookCreate(UserBook):
    book: Book
    reading_start_date: Optional[str] = Field(
        default=None,
        description="Required format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS.sssZ",
    )
    reading_end_date: Optional[str] = Field(
        default=None,
        description="Required format: YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS.sssZ",
    )

    @field_validator("reading_start_date", "reading_end_date", mode="before")
    def format_dates(cls, value: Optional[str]):
        return format_date_string_to_isoformat(value)


class UserBookCreateDb(UserBook):

    @field_serializer("reading_start_date", "reading_end_date")
    def serialize_dates(self, value: Optional[str], _info):
        if value is None:
            return None
        return datetime.fromisoformat(value)

    pass


@exclude_fields("user_id", "book_id")
class UserBookUpdate(Book, UserBook):
    pass
