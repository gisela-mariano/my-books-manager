from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.domain.user_book_annotation_service import (
    UserBookAnnotationService,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotationJoinUserBook,
    UserBookAnnotationUpdate,
)
from src.core.utils.database.postgres import join_result_to_dict


class UserBookAnnotationUpdateUseCase:
    def __init__(
        self,
        repository: UserBookAnnotationRepository,
        service: UserBookAnnotationService,
    ) -> None:
        self.repository = repository
        self.service = service

    async def execute(
        self, id: str, payload: UserBookAnnotationUpdate
    ) -> dict[UserBookAnnotationJoinUserBook]:
        await self.service.verify_user_book_annotation_exists_by_id(id=id)

        update_data = UserBookAnnotationUpdate(
            **payload.model_dump(exclude_unset=True)
        ).model_dump(exclude_unset=True)

        result = await self.repository.update(
            id=id, user_book_annotation=update_data, join_user_book=True
        )

        return join_result_to_dict(UserBookAnnotationJoinUserBook, result)
