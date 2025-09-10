from abc import ABC, abstractmethod

from src.core.components.v1.books.infra.schemas.book import BookCreate, BookDb


class BookRepository(ABC):
    @abstractmethod
    def create(self, book: dict[BookCreate]) -> dict[BookDb]:
        pass

    @abstractmethod
    def get_by_isbn_or_title(self, isbn: str = None, title: str = None) -> dict[BookDb]:
        pass
