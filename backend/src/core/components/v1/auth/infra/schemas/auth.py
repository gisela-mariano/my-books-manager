from typing import Optional

from src.core.utils.models.base import BaseConfig


class Token(BaseConfig):
    access_token: str
    token_type: str


class TokenUserData(BaseConfig):
    id: str = None
    username: Optional[str] = None
    email: Optional[str] = None


class AuthLogin(BaseConfig):
    email: str
    password: str
