from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationCreate,
    UserBookAnnotationDb,
    UserBookAnnotationJoinUserBook,
    UserBookAnnotationUpdate,
)


class UserBookAnnotationRepository(ABC):
    @abstractmethod
    def create(
        self, user_book_annotation: dict[UserBookAnnotationCreate]
    ) -> dict[UserBookAnnotationDb]:
        pass

    @abstractmethod
    def get_by_id(
        self, id: str, join_user_book: bool = True
    ) -> Optional[UserBookAnnotationJoinUserBook]:
        pass

    @abstractmethod
    def get_user_book_annotations_by_user_book_id(
        self, user_book_id: str, limit=25, offset=0, join_user_book: bool = True
    ) -> List[UserBookAnnotationJoinUserBook]:
        pass

    @abstractmethod
    def update(
        self,
        id: str,
        user_book_annotation: dict[UserBookAnnotationUpdate],
        join_user_book: bool = False,
    ) -> dict[UserBookAnnotationJoinUserBook]:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
