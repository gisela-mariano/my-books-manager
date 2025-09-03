from typing import Union

from pydantic import BaseModel
from src.core.utils.models.base import BaseConfig


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config(BaseConfig):
        pass


class TokenData(BaseModel):
    username: Union[str, None] = None
    email: Union[str, None] = None

    class Config(BaseConfig):
        pass


class AuthLogin(BaseModel):
    email: str
    password: str

    class Config(BaseConfig):
        pass
