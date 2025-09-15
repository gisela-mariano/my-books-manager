from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationCreate,
    UserBookAnnotationJoinUserBook,
)
from src.core.components.v1.user_books.domain.user_book_service import UserBookService
from src.core.utils.database.postgres import join_result_to_dict


class UseBookAnnotationCreateUseCase:
    def __init__(
        self,
        repository: UserBookAnnotationRepository,
        user_book_service: UserBookService,
    ) -> None:
        self.repository = repository
        self.user_book_service = user_book_service

    async def execute(
        self, user_book_annotation: UserBookAnnotationCreate
    ) -> dict[UserBookAnnotationJoinUserBook]:
        await self.user_book_service.verify_user_book_exists_by_id(
            id=user_book_annotation.user_book_id
        )

        created_user_book_annotation = await self.repository.create(
            user_book_annotation=user_book_annotation.model_dump()
        )

        result = await self.repository.get_by_id(
            id=created_user_book_annotation.get("id")
        )

        return join_result_to_dict(UserBookAnnotationJoinUserBook, result)
