from typing import List, Optional

from sqlalchemy import join, select
from src.core.components.v1.books.infra.models.book import books
from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.infra.models.user_book_annotations import (
    user_book_annotations,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationCreate,
    UserBookAnnotationDb,
    UserBookAnnotationJoinUserBook,
    UserBookAnnotationUpdate,
)
from src.core.components.v1.user_books.infra.models.user_books import user_books
from src.core.persistence.database.postgres_database import Database as PostgresDatabase
from src.core.repositories.postgres_base_repository import PostgresBaseRepository
from src.core.utils.database.postgres import alias_columns
from src.core.utils.error_report import get_exception_metadata
from src.core.utils.exceptions.errors import DbError


class PostgresUserBookAnnotationRepository(
    PostgresBaseRepository, UserBookAnnotationRepository
):
    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create(
        self, user_book_annotation: dict[UserBookAnnotationCreate]
    ) -> dict[UserBookAnnotationDb]:
        try:
            return await self.create_data(
                table=user_book_annotations, payload=user_book_annotation
            )
        except Exception as e:
            raise DbError(
                message="Error when creating user book annotation",
                metadata=[get_exception_metadata(e)],
            )

    async def get_by_id(
        self, id: str, join_user_book: bool = True
    ) -> Optional[UserBookAnnotationJoinUserBook]:
        try:
            if join_user_book:
                j = join(
                    user_book_annotations,
                    user_books,
                    user_book_annotations.c.user_book_id == user_books.c.id,
                    full=True,
                )

                j_book = join(
                    j,
                    books,
                    user_books.columns.book_id == books.columns.id,
                    full=True,
                )

                query = (
                    select(
                        *user_book_annotations.c,
                        *alias_columns(user_books, "user_book"),
                        *alias_columns(books, "user_book__book")
                    )
                    .select_from(j_book)
                    .where(user_book_annotations.c.id == id)
                )
            else:
                query = select(user_book_annotations).where(
                    user_book_annotations.c.id == id
                )

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book annotation by id",
                metadata=[get_exception_metadata(e)],
            )

    async def get_user_book_annotations_by_user_book_id(
        self, user_book_id: str, limit=25, offset=0, join_user_book: bool = True
    ) -> List[UserBookAnnotationJoinUserBook]:
        try:
            if join_user_book:
                j = join(
                    user_book_annotations,
                    user_books,
                    user_book_annotations.c.user_book_id == user_books.c.id,
                    full=True,
                )

                j_book = join(
                    j,
                    books,
                    user_books.columns.book_id == books.columns.id,
                    full=True,
                )

                query = (
                    select(
                        *user_book_annotations.c,
                        *alias_columns(user_books, "user_book"),
                        *alias_columns(books, "user_book__book")
                    )
                    .select_from(j_book)
                    .where(user_book_annotations.c.user_book_id == user_book_id)
                )
            else:
                query = select(user_book_annotations).where(
                    user_book_annotations.c.user_book_id == user_book_id
                )

            query = query.limit(limit).offset(offset)

            result = await self.db.fetch_all(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user book annotations by user book id",
                metadata=[get_exception_metadata(e)],
            )

    async def update(
        self,
        id: str,
        user_book_annotation: dict[UserBookAnnotationUpdate],
        join_user_book: bool = False,
    ) -> dict[UserBookAnnotationJoinUserBook]:
        try:
            result = await self.update_data(
                table=user_book_annotations, id=id, payload=user_book_annotation
            )

            if join_user_book:
                result = await self.get_by_id(id=id)

            return result
        except Exception as e:
            raise DbError(
                message="Error when updating user book annotation",
                metadata=[get_exception_metadata(e)],
            )

    async def delete(self, id: str) -> bool:
        try:
            result = await self.delete_data(table=user_book_annotations, id=id)

            return result
        except Exception as e:
            raise DbError(
                message="Error when deleting user book annotation",
                metadata=[get_exception_metadata(e)],
            )
