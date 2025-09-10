from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookCreateDb,
    UserBookDb,
)
from src.core.utils.exceptions.errors import AlreadyRegisteredError


class UserBookService:
    def __init__(self, repository: UserBookRepository):
        self.repository = repository

    async def create_or_raise(self, user_book: UserBookCreateDb) -> dict[UserBookDb]:
        already_registered_user_book = await self.repository.get_by_user_id_and_book_id(
            user_id=user_book.user_id, book_id=user_book.book_id
        )

        if already_registered_user_book:
            raise AlreadyRegisteredError(
                f"User book already registered for user {user_book.user_id} and book {user_book.book_id}"
            )

        created_user_book = await self.repository.create(user_book.model_dump())

        return (
            UserBookDb(**created_user_book).model_dump(by_alias=True)
            if created_user_book
            else None
        )
