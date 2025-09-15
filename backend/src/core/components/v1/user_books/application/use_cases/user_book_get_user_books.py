from asyncio import gather

from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookJoinBook,
    UserBooksJoinBookPaginatedResponse,
)
from src.core.components.v1.users.domain.user_service import UserService
from src.core.utils.database.postgres import join_result_to_dict


class UserBookGetUserBooksUseCase:
    def __init__(
        self,
        repository: UserBookRepository,
        user_service: UserService,
    ) -> None:
        self.repository = repository
        self.user_service = user_service

    async def execute(self, user_id: str, limit=25, offset=0) -> list[UserBookJoinBook]:
        await self.user_service.verify_user_exists_by_id(id=user_id)

        user_books, total = await gather(
            self.repository.get_user_books_by_user_id(
                user_id=user_id, limit=limit, offset=offset
            ),
            self.repository.get_user_books_total_by_user_id(user_id=user_id),
        )

        return UserBooksJoinBookPaginatedResponse(
            user_books=[
                join_result_to_dict(UserBookJoinBook, user_book)
                for user_book in user_books
            ],
            total=total,
        )
