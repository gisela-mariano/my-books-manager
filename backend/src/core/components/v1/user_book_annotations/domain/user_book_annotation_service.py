from src.core.components.v1.user_book_annotations.domain.user_book_annotation_repository import (
    UserBookAnnotationRepository,
)
from src.core.components.v1.user_book_annotations.infra.schemas.user_book_annotation import (
    UserBookAnnotation,
)
from src.core.utils.exceptions.errors import AssetNotFoundError


class UserBookAnnotationService:
    def __init__(self, repository: UserBookAnnotationRepository):
        self.repository = repository

    async def verify_user_book_annotation_exists_by_id(
        self, id: str
    ) -> UserBookAnnotation:
        """Verify if user book annotation exists by id

        Args:
            id (str): user book annotation id

        Raises:
            AssetNotFoundError: Raises if user book annotation does not exist

        Returns:
            UserBookDb: Return user book annotation if exists
        """

        user = await self.repository.get_by_id(id=id)

        if not user:
            raise AssetNotFoundError(f"User book annotation with id {id} not found")

        return user
