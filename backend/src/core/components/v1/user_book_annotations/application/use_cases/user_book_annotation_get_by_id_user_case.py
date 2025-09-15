from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationJoinUserBook,
)
from src.core.utils.database.postgres import join_result_to_dict


class UserBookAnnotationGetByIdUseCase:
    def __init__(
        self,
        repository: UserBookAnnotationRepository,
    ) -> None:
        self.repository = repository

    async def execute(self, id: str) -> dict[UserBookAnnotationJoinUserBook]:
        user_book_annotation = await self.repository.get_by_id(id=id)

        return (
            join_result_to_dict(UserBookAnnotationJoinUserBook, user_book_annotation)
            if user_book_annotation
            else None
        )
