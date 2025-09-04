from asyncio import gather
from typing import Union

from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.schemas.user import UserDb
from src.core.utils.exceptions.errors import AlreadyRegisteredError, AssetNotFoundError


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def verify_already_registered(
        self,
        email: Union[str, None] = None,
        username: Union[str, None] = None,
        id: Union[str, None] = None,
    ) -> bool:
        """Verify if user already exists by email or username

        If the ID is provided, the verification will take into account whether it is the user's own data (for an update, for example). If it is not provided, only the email or username will be taken into account (for a create, for example).


        Args:
            id (Union[str, None])
            email (str)
            username (str)

        Raises:
            AlreadyRegisteredError: Raises if user with same email or username already exists

        Returns:
            bool (False): Return if user does not exist
        """
        tasks = {}

        if email:
            tasks["email"] = self.repository.get_by_email(email)
        if username:
            tasks["username"] = self.repository.get_by_username(username)

        results = await gather(*tasks.values())
        lookup = dict(zip(tasks.keys(), results))

        for field, user in lookup.items():
            if user and (id is None or user.get("id") != id):
                raise AlreadyRegisteredError(
                    f"User with {field} {email if field == 'email' else username} already registered"
                )

        return False

    async def verify_user_exists_by_id(self, id: str) -> UserDb:
        """Verify if user exists by id

        Args:
            id (str): user id

        Raises:
            AssetNotFoundError: Raises if user does not exist

        Returns:
            UserDb: Return user if exists
        """

        user = await self.repository.get_by_id(id=id)

        if not user:
            raise AssetNotFoundError(f"User with id {id} not found")

        return user
