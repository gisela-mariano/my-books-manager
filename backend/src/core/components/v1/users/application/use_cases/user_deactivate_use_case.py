from asyncio import gather

from src.core.components.v1.auth.domain.auth_service import AuthService
from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.domain.user_service import UserService
from src.core.components.v1.users.infra.schemas.user import UserDbResponse, UserUpdate
from src.core.utils.exceptions.errors import InvalidInputProvidedError


class UserDeactivateUseCase:

    def __init__(
        self,
        repository: UserRepository,
        service: UserService,
    ):
        self.repository = repository
        self.service = service

    async def execute(self, id: str) -> None:

        await self.service.verify_user_exists_by_id(id=id)

        await self.repository.update(
            id=id,
            user={"is_active": False},
        )

        return
