from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.domain.user_book_annotation_service import (
    UserBookAnnotationService,
)


class UserBookAnnotationDeleteUseCase:
    def __init__(
        self,
        repository: UserBookAnnotationRepository,
        service: UserBookAnnotationService,
    ) -> None:
        self.repository = repository
        self.service = service

    async def execute(self, id: str) -> None:
        await self.service.verify_user_book_annotation_exists_by_id(id=id)

        await self.repository.delete(id=id)
