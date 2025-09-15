from abc import ABC, abstractmethod
from typing import Optional, Union

from src.core.components.v1.users.infra.schemas.user import (
    UserCreate,
    UserDb,
    UserUpdate,
)


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: dict[UserCreate]) -> dict[UserDb]:
        pass

    @abstractmethod
    def get_by_id(self, id: str, verify_activity: bool = True) -> Optional[UserDb]:
        pass

    @abstractmethod
    def get_by_email(
        self, email: str, verify_activity: bool = True
    ) -> Union[UserDb, None]:
        pass

    @abstractmethod
    def get_by_username(
        self, username: str, verify_activity: bool = True
    ) -> Union[UserDb, None]:
        pass

    @abstractmethod
    def update(self, id: str, user: dict[UserUpdate]) -> dict[UserDb]:
        pass

    @abstractmethod
    def deactivate(self, id: str) -> bool:
        pass
