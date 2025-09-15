from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.schemas.user import UserCreate, UserDbResponse
from src.core.utils.exceptions.errors import AlreadyRegisteredError, AssetNotFoundError


class UserFindByIdUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, id: str) -> UserDbResponse:
        user = await self.repository.get_by_id(id)

        if not user:
            raise AssetNotFoundError(f"User with id {id} not found")

        return UserDbResponse(**user).model_dump(by_alias=True)
