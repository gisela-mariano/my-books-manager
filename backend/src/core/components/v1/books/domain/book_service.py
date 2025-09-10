from src.core.components.v1.books.domain.book_repository import BookRepository
from src.core.components.v1.books.infra.schemas.book import BookCreate, BookDb


class BookService:
    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    async def create_or_get(self, book: BookCreate) -> dict[BookDb]:
        isbn = book.isbn_10 or book.isbn_13

        registered_book = await self.repository.get_by_isbn_or_title(
            isbn=isbn, title=book.title
        )

        result = {}

        if registered_book:
            result = registered_book
        else:
            result = await self.repository.create(book.model_dump())

        return BookDb(**result).model_dump(by_alias=True) if result else None
