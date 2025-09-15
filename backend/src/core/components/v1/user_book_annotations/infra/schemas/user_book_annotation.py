from typing import List

from pydantic import Field
from src.core.components.v1.user_books.infra.schemas.user_book import UserBookJoinBook
from src.core.utils.models.base import AllOptional, BaseConfig, BaseInDb, exclude_fields


class UserBookAnnotation(BaseConfig):
    user_book_id: str
    note: str


class UserBookAnnotationDb(UserBookAnnotation, BaseInDb):
    pass


class UserBookAnnotationCreate(UserBookAnnotation):
    note: str = Field(min_length=3)
    pass


@exclude_fields("user_book_id")
class UserBookAnnotationUpdate(UserBookAnnotation, metaclass=AllOptional):
    pass


class UserBookAnnotationJoinUserBook(UserBookAnnotationDb):
    user_book: UserBookJoinBook


class UserBookAnnotationsPaginatedResponse(BaseConfig):
    user_book_annotations: List[UserBookAnnotationJoinUserBook]
    total: int
