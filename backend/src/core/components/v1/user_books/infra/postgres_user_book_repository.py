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
from src.core.utils.error_report import get_exception_metadata
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
                metadata=[get_exception_metadata(e)],
            )

    async def get_by_id(
        self, id: str, join_book: bool = True
    ) -> Optional[UserBookJoinBook]:
        try:

            if join_book:
                j = join(
                    user_books,
                    books,
                    user_books.columns.book_id == books.columns.id,
                    full=True,
                )

                query = (
                    select(*user_books.columns, *alias_columns(books, "book"))
                    .select_from(j)
                    .where(
                        user_books.c.id == id,
                    )
                )
            else:
                query = select(user_books).where(
                    user_books.c.id == id,
                )

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book by id",
                metadata=[get_exception_metadata(e)],
            )

    async def get_by_user_id_and_book_id(
        self, user_id: str, book_id: str, join_book: bool = True
    ) -> Optional[UserBookJoinBook]:
        try:
            if join_book:
                j = join(
                    user_books,
                    books,
                    user_books.columns.book_id == books.columns.id,
                    full=True,
                )

                query = (
                    select(*user_books.columns, *alias_columns(books, "book"))
                    .select_from(j)
                    .where(
                        user_books.columns.user_id == user_id,
                        user_books.columns.book_id == book_id,
                    )
                )
            else:
                query = select(user_books).where(
                    user_books.columns.user_id == user_id,
                    user_books.columns.book_id == book_id,
                )

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book by user id and book id",
                metadata=[get_exception_metadata(e)],
            )

    async def get_user_books_by_user_id(
        self, user_id: str, limit=25, offset=0, join_book: bool = True
    ) -> List[UserBookJoinBook]:
        try:
            if join_book:
                j = join(
                    user_books, books, user_books.c.book_id == books.c.id, full=True
                )

                query = (
                    select(*user_books.c, *alias_columns(books, "book"))
                    .select_from(j)
                    .where(user_books.c.user_id == user_id)
                )
            else:
                query = select(user_books).where(user_books.c.user_id == user_id)

            query = query.limit(limit).offset(offset)

            result = await self.db.fetch_all(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user books by user id",
                metadata=[get_exception_metadata(e)],
            )

    async def update(
        self, id: str, user_book: dict[UserBookUpdate], join_book: bool = False
    ) -> dict[UserBookJoinBook]:
        try:
            result = await self.update_data(table=user_books, id=id, payload=user_book)

            if join_book:
                result = await self.get_by_id(id=id)

            return result
        except Exception as e:
            raise DbError(
                message="Error when updating user book",
                metadata=[get_exception_metadata(e)],
            )

    async def delete(self, id: str) -> bool:
        try:
            result = await self.delete_data(table=user_books, id=id)

            return result
        except Exception as e:
            raise DbError(
                message="Error when deleting user book",
                metadata=[get_exception_metadata(e)],
            )
