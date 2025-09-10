from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookCreate,
    UserBookJoinBook,
    UserBookUpdate,
)


class UserBookRepository(ABC):
    @abstractmethod
    def create(self, user_book: dict[UserBookCreate]) -> dict[UserBookJoinBook]:
        pass

    @abstractmethod
    def get_by_id(self, id: str, join_book: bool = True) -> Optional[UserBookJoinBook]:
        pass

    @abstractmethod
    def get_by_user_id_and_book_id(
        self, user_id: str, book_id: str, join_book: bool = True
    ) -> Optional[UserBookJoinBook]:
        pass

    @abstractmethod
    def get_user_books_by_user_id(
        self, user_id: str, limit=25, offset=0, join_book: bool = True
    ) -> List[UserBookJoinBook]:
        pass

    @abstractmethod
    def update(
        self, id: str, user_book: dict[UserBookUpdate], join_book: bool = False
    ) -> dict[UserBookJoinBook]:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
