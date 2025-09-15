from typing import List

from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationJoinUserBook,
)
from src.core.utils.database.postgres import join_result_to_dict


class UserBookAnnotationGetAnnotationsUseCase:
    def __init__(
        self,
        repository: UserBookAnnotationRepository,
    ) -> None:
        self.repository = repository

    async def execute(
        self, user_book_id: str, limit: int = 25, offset: int = 0
    ) -> List[UserBookAnnotationJoinUserBook]:
        user_book_annotations = (
            await self.repository.get_user_book_annotations_by_user_book_id(
                user_book_id=user_book_id, limit=limit, offset=offset
            )
        )

        return [
            join_result_to_dict(UserBookAnnotationJoinUserBook, user_book_annotation)
            for user_book_annotation in user_book_annotations
        ]
