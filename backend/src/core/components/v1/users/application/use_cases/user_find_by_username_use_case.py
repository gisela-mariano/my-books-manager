from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.schemas.user import UserDbResponse
from src.core.utils.exceptions.errors import AssetNotFoundError


class UserFindByUsernameUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, username: str) -> UserDbResponse:
        user = await self.repository.get_by_username(username=username)

        if not user:
            raise AssetNotFoundError(f"User with username {username} not found")

        return UserDbResponse(**user).model_dump(by_alias=True)
