from pydantic import BaseModel, EmailStr, Field, field_validator
from src.core.components.v1.users.infra.models.validators import (
    ValidateStringEmptyAndLimit,
    ValidateStrongPassword,
)
from src.core.utils.exceptions.errors import ValidationPayloadError
from src.core.utils.models.base import AllOptional, BaseConfig, BaseInDb, exclude_fields
from src.core.utils.validators import is_valid_password


class User(BaseModel):
    name: str = Field(max_length=255)
    lastname: str = Field(max_length=255)
    username: str = Field(max_length=255)
    email: EmailStr = Field(max_length=60)
    password: str

    @field_validator("name")
    def validate_name(cls, value):
        return ValidateStringEmptyAndLimit(
            max_length=255, value=value, min_length=2
        ).value

    @field_validator("lastname")
    def validate_lastname(cls, value):
        return ValidateStringEmptyAndLimit(max_length=255, value=value).value

    @field_validator("username")
    def validate_username(cls, value):
        return ValidateStringEmptyAndLimit(max_length=255, value=value).value

    class Config(BaseConfig):
        pass


class UserDb(User, BaseInDb):
    is_active: bool = Field(default=True)
    pass


@exclude_fields("password")
class UserDbResponse(UserDb):

    class Config(BaseConfig):
        pass


class UserCreate(User):
    password: str = Field(max_length=255)

    @field_validator("password")
    def validate_password(cls, value):
        return ValidateStrongPassword(value=value).value


@exclude_fields("email")
class UserUpdate(User, metaclass=AllOptional):
    pass
