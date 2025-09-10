from sqlalchemy import select
from src.core.components.v1.books.domain.book_repository import BookRepository
from src.core.components.v1.books.infra.models.book import books
from src.core.components.v1.books.infra.schemas.book import BookCreate, BookDb
from src.core.persistence.database.postgres_database import Database as PostgresDatabase
from src.core.repositories.postgres_base_repository import PostgresBaseRepository
from src.core.utils.error_report import (
    get_caller_info,
    get_caller_name,
    get_caller_payload,
)
from src.core.utils.exceptions.errors import DbError


class PostgresBookRepository(PostgresBaseRepository, BookRepository):

    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create(self, user: dict[BookCreate]) -> dict[BookDb]:
        try:
            return await self.create_data(table=books, payload=user)
        except Exception as e:
            raise DbError(
                message="Error when creating book",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_isbn_or_title(
        self, isbn: str = None, title: str = None
    ) -> dict[BookDb]:
        try:
            where_clause = (
                books.c.isbn_10 == isbn
                if isbn and len(isbn) == 10
                else (
                    books.c.isbn_13 == isbn
                    if isbn and len(isbn) == 13
                    else books.c.title == title
                )
            )

            query = select(books).where(where_clause)

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting book by isbn or title",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )
