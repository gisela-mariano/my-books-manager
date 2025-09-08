from sqlalchemy import select
from src.core.components.v1.users.domain.user_repository import UserRepository
from src.core.components.v1.users.infra.models.user import users
from src.core.components.v1.users.infra.schemas.user import (
    UserCreate,
    UserDb,
    UserUpdate,
)
from src.core.persistence.database.postgres_database import Database as PostgresDatabase
from src.core.repositories.postgres_base_repository import PostgresBaseRepository
from src.core.utils.error_report import (
    get_caller_info,
    get_caller_name,
    get_caller_payload,
)
from src.core.utils.exceptions.errors import DbError


class PostgresUserRepository(PostgresBaseRepository, UserRepository):

    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create(self, user: dict[UserCreate]) -> dict[UserDb]:
        try:
            return await self.create_data(table=users, payload=user)
        except Exception as e:
            raise DbError(
                message="Error when creating user",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_id(self, id: str, verify_activity: bool = True) -> dict[UserDb]:
        """
        Retrieve a user by username, optionally verifying if they are active (by default will verify activity).
        """
        try:
            query = select(users).where(users.columns.id == id)

            if verify_activity:
                query = query.where(users.columns.is_active == True)

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user by id",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_email(
        self, email: str, verify_activity: bool = True
    ) -> dict[UserDb]:
        """
        Retrieve a user by username, optionally verifying if they are active (by default will verify activity).
        """
        try:
            query = select(users).where(users.columns.email == email)

            if verify_activity:
                query = query.where(users.columns.is_active == True)

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user by email",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def get_by_username(
        self, username: str, verify_activity: bool = True
    ) -> dict[UserDb]:
        """
        Retrieve a user by username, optionally verifying if they are active (by default will verify activity).
        """
        try:
            query = select(users).where(users.columns.username == username)

            if verify_activity:
                query = query.where(users.columns.is_active == True)

            result = await self.db.fetch_one(query)

            return result
        except Exception as e:
            raise DbError(
                message="Error when getting user by username",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def update(self, id: str, user: dict[UserUpdate]) -> dict[UserDb]:
        try:
            return await self.update_data(table=users, id=id, payload=user)
        except Exception as e:
            raise DbError(
                message="Error when updating user",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )

    async def deactivate(self, id: str) -> dict[UserDb]:
        try:
            payload = {"is_active": False}

            return await self.update_data(table=users, id=id, payload=payload)
        except Exception as e:
            raise DbError(
                message="Error when deactivating user",
                metadata=[
                    {
                        "exception": str(e),
                        "payload": get_caller_payload(),
                        "where": get_caller_name(),
                        "from": get_caller_info(),
                    }
                ],
            )
