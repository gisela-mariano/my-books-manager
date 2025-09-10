from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.domain.user_book_service import UserBookService
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookJoinBook,
    UserBookUpdate,
    UserBookUpdateDb,
)
from src.core.utils.database.postgres import join_result_to_dict


class UserBookUpdateUseCase:
    def __init__(
        self,
        repository: UserBookRepository,
        service: UserBookService,
    ) -> None:
        self.repository = repository
        self.service = service

    async def execute(self, id: str, payload: UserBookUpdate) -> dict[UserBookJoinBook]:
        await self.service.verify_user_book_exists_by_id(id=id)

        update_data = UserBookUpdateDb(
            **payload.model_dump(exclude_unset=True)
        ).model_dump(exclude_unset=True)

        updated_user_book = await self.repository.update(
            id=id, user_book=update_data, join_book=True
        )

        return join_result_to_dict(UserBookJoinBook, updated_user_book, "b", "book")
