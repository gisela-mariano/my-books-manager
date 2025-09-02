from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.schemas.user import UserCreate, UserDbResponse
from src.core.utils.exceptions.errors import AlreadyRegisteredError


class UserCreationUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def execute(self, user: UserCreate) -> UserDbResponse:
        already_registered = await self.repository.get_by_email(user.email)

        if already_registered:
            raise AlreadyRegisteredError(
                f"User with email {user.email} already registered"
            )

        created_user = await self.repository.create(user.model_dump())

        return UserDbResponse(**created_user).model_dump(by_alias=True)
