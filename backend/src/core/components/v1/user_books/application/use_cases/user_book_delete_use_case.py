from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.domain.user_book_service import UserBookService


class UserBookDeleteUseCase:
    def __init__(
        self,
        repository: UserBookRepository,
        service: UserBookService,
    ) -> None:
        self.repository = repository
        self.service = service

    async def execute(self, id: str) -> None:
        await self.service.verify_user_book_exists_by_id(id=id)

        await self.repository.delete(id=id)
