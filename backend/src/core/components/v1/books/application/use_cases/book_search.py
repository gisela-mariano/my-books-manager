from typing import Optional

from src.core.components.v1.books.infra.schemas.book import BookSearchPaginatedResponse
from src.core.components.v1.books.utils.book_converters import volume_to_book
from src.core.providers.google_books_api import GoogleBooksApiProvider


class BookSearchUseCase:
    def __init__(self, google_books_provider: GoogleBooksApiProvider):
        self.google_books_provider = google_books_provider

    async def execute(
        self,
        search_term: str = None,
        author: Optional[str] = None,
        publisher: Optional[str] = None,
        title: Optional[str] = None,
        isbn: Optional[str] = None,
        limit: Optional[int] = 25,
        offset: Optional[int] = 0,
    ):

        query = ""

        if search_term:
            query += f"{search_term}"

        if author:
            query += f"+inauthor:{author}"

        if publisher:
            query += f"+inpublisher:{publisher}"

        if title:
            query += f"+intitle:{title}"

        if isbn:
            query += f"+isbn:{isbn}"

        result = self.google_books_provider.search_volume(
            query=query, limit=limit, offset=offset
        )

        books = [volume_to_book(volume=volume.volume_info) for volume in result.items]

        return BookSearchPaginatedResponse(
            books=books, total=result.total_items
        ).model_dump(by_alias=True)
