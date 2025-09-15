from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.schemas.user import UserDbResponse
from src.core.utils.exceptions.errors import AssetNotFoundError


class UserFindByEmailUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, email: str) -> UserDbResponse:
        user = await self.repository.get_by_email(email=email)

        if not user:
            raise AssetNotFoundError(f"User with email {email} not found")

        return UserDbResponse(**user).model_dump(by_alias=True)
