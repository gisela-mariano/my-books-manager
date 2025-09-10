from typing import List, Optional

from sqlalchemy import join, select
from src.core.components.v1.books.infra.models.book import books
from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.infra.models.user_books import user_books
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookCreate,
    UserBookJoinBook,
    UserBookUpdate,
)
from src.core.persistence.database.postgres_database import Database as PostgresDatabase
from src.core.repositories.postgres_base_repository import PostgresBaseRepository
from src.core.utils.database.postgres import alias_columns
from src.core.utils.error_report import (
    get_caller_info,
    get_caller_name,
    get_caller_payload,
)
from src.core.utils.exceptions.errors import DbError


class PostgresUserBookRepository(PostgresBaseRepository, UserBookRepository):

    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create(self, user_book: dict[UserBookCreate]) -> dict[UserBookJoinBook]:
        try:
            return await self.create_data(table=user_books, payload=user_book)
        except Exception as e:
            raise DbError(
                message="Error when creating user book",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_id(
        self, id: str, join_book: bool = True
    ) -> Optional[UserBookJoinBook]:
        try:
            j = join(
                user_books,
                books,
                user_books.columns.book_id == books.columns.id,
                full=True,
            )

            query = select(user_books).where(
                user_books.c.id == id,
            )

            if join_book:
                query = (
                    select(*user_books.columns, *alias_columns(books, "b"))
                    .select_from(j)
                    .where(
                        user_books.c.id == id,
                    )
                )

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book by id",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_user_id_and_book_id(
        self, user_id: str, book_id: str, join_book: bool = True
    ) -> Optional[UserBookJoinBook]:
        try:
            j = join(
                user_books,
                books,
                user_books.columns.book_id == books.columns.id,
                full=True,
            )

            query = select(user_books).where(
                user_books.columns.user_id == user_id,
                user_books.columns.book_id == book_id,
            )

            if join_book:
                query = (
                    select(*user_books.columns, *alias_columns(books, "b"))
                    .select_from(j)
                    .where(
                        user_books.columns.user_id == user_id,
                        user_books.columns.book_id == book_id,
                    )
                )

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book by user id and book id",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_user_books_by_user_id(
        self, user_id: str, join_book: bool = True
    ) -> List[UserBookJoinBook]:
        try:
            j = join(
                user_books,
                books,
                user_books.columns.book_id == books.columns.id,
                full=True,
            )

            query = select(user_books).where(
                user_books.columns.user_id == user_id,
            )

            if join_book:
                query = (
                    select(*user_books.columns, *alias_columns(books, "b"))
                    .select_from(j)
                    .where(
                        user_books.columns.user_id == user_id,
                    )
                )

            result = await self.db.fetch_all(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user books by user id",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def update(
        self, id: str, user_book: dict[UserBookUpdate]
    ) -> dict[UserBookJoinBook]:
        pass

    async def delete(self, id: str) -> bool:
        pass
