from typing import Optional

from pydantic import EmailStr, Field, field_validator, model_validator
from src.core.components.v1.users.infra.models.validators import (
    ValidateStringEmptyAndLimit,
    ValidateStrongPassword,
)
from src.core.utils.exceptions.errors import ValidationPayloadError
from src.core.utils.models.base import AllOptional, BaseConfig, BaseInDb, exclude_fields


class User(BaseConfig):
    name: str = Field(max_length=255)
    lastname: str = Field(max_length=255)
    username: str = Field(max_length=255)
    email: EmailStr = Field(max_length=60)

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


class UserDb(User, BaseInDb):
    is_active: bool = Field(default=True)
    hash_password: str


@exclude_fields("hash_password")
class UserDbResponse(UserDb):
    pass


class UserCreate(User):
    password: str = Field(max_length=255)

    @field_validator("password")
    def validate_password(cls, value):
        return ValidateStrongPassword(value=value).value


class UserUpdate(UserCreate, metaclass=AllOptional):
    old_password: Optional[str]

    @model_validator(mode="after")
    def check_passwords(self):
        if self.old_password and not self.password:
            raise ValidationPayloadError(
                "Password is required when old password is provided"
            )

        if self.password and not self.old_password:
            raise ValidationPayloadError(
                "Old password is required when password is provided"
            )

        return self
