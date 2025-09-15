from src.core.components.v1.auth.domain.auth_service import AuthService
from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.domain.user_service import UserService
from src.core.components.v1.users.infra.schemas.user import UserCreate, UserDbResponse


class UserCreateUseCase:
    def __init__(
        self,
        repository: UserRepository,
        service: UserService,
        auth_service: AuthService,
    ):
        self.repository = repository
        self.service = service
        self.auth_service = auth_service

    async def execute(self, user: UserCreate) -> UserDbResponse:

        await self.service.verify_already_registered(
            email=user.email, username=user.username
        )

        hashed_password = self.auth_service.get_password_hash(user.password)
        del user.password

        created_user = await self.repository.create(
            {**user.model_dump(), "hashed_password": hashed_password}
        )

        return UserDbResponse(**created_user).model_dump(by_alias=True)
