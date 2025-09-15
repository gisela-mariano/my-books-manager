from src.core.components.v1.books.domain.book_service import BookService
from src.core.components.v1.books.infra.schemas.book import BookCreate
from src.core.components.v1.user_books.domain.user_book_repository import (
    UserBookRepository,
)
from src.core.components.v1.user_books.domain.user_book_service import UserBookService
from src.core.components.v1.user_books.infra.schemas.user_book import (
    UserBookCreate,
    UserBookCreateDb,
    UserBookJoinBook,
)
from src.core.components.v1.users.domain.user_service import UserService
from src.core.utils.database.postgres import join_result_to_dict


class UserBookCreateUseCase:
    def __init__(
        self,
        repository: UserBookRepository,
        service: UserBookService,
        book_service: BookService,
        user_service: UserService,
    ) -> None:
        self.repository = repository
        self.service = service
        self.book_service = book_service
        self.user_service = user_service

    async def execute(
        self, payload: UserBookCreate, user_id: str
    ) -> dict[UserBookJoinBook]:
        await self.user_service.verify_user_exists_by_id(id=user_id)

        dict_payload = payload.model_dump()

        create_book_payload = BookCreate(**dict_payload.get("book"))

        book = await self.book_service.create_or_get(book=create_book_payload)

        if book:
            dict_payload["book_id"] = book.get("id")

            create_user_book_payload = UserBookCreateDb(**dict_payload, user_id=user_id)

            created_user_book = await self.service.create_or_raise(
                user_book=create_user_book_payload
            )

            user_book = await self.repository.get_by_id(id=created_user_book.get("id"))

            return join_result_to_dict(UserBookJoinBook, user_book)
        else:
            return None
