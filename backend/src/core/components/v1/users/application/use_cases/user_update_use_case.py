from asyncio import gather

from src.core.components.v1.auth.domain.auth_service import AuthService
from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.domain.user_service import UserService
from src.core.components.v1.users.infra.schemas.user import UserDbResponse, UserUpdate
from src.core.utils.exceptions.errors import InvalidInputProvidedError


class UserUpdateUseCase:

    def __init__(
        self,
        repository: UserRepository,
        service: UserService,
        auth_service: AuthService,
    ):
        self.repository = repository
        self.service = service
        self.auth_service = auth_service

    async def execute(self, id: str, user: UserUpdate) -> UserDbResponse:

        _, user_db = await gather(
            self.service.verify_already_registered(
                id=id, email=user.email, username=user.username
            ),
            self.service.verify_user_exists_by_id(id=id),
        )

        update_data = {**user.model_dump(exclude_unset=True)}

        if user.password:
            passwords_match = self.auth_service.verify_password(
                user.old_password, user_db.get("hashed_password")
            )

            if not passwords_match:
                raise InvalidInputProvidedError(
                    "Old password does not match with user password"
                )

            hashed_password = self.auth_service.get_password_hash(user.password)

            update_data.update({"hashed_password": hashed_password})
            del update_data["old_password"]
            del update_data["password"]

        updated_user = await self.repository.update(
            id=id,
            user=update_data,
        )

        return UserDbResponse(**updated_user).model_dump(by_alias=True)
