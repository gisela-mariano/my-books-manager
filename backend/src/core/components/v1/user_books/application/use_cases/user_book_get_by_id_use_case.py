from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.infra.schemas.user_book import UserBookJoinBook
from src.core.components.v1.users.domain.user_service import UserService
from src.core.utils.database.postgres import join_result_to_dict


class UserBookGetByIdUseCase:
    def __init__(
        self,
        repository: UserBookRepository,
    ) -> None:
        self.repository = repository

    async def execute(self, id: str) -> dict[UserBookJoinBook]:
        user_book = await self.repository.get_by_id(id=id)

        return join_result_to_dict(UserBookJoinBook, user_book, "b", "book")
