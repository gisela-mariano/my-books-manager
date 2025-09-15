from typing import Union

from pydantic import BaseModel, ValidationInfo, field_validator
from src.core.utils.validators import is_valid_password


class ValidateStringEmptyAndLimit(BaseModel):
    min_length: int = 0
    max_length: Union[int, float] = float("inf")
    value: Union[str, None] = None

    @field_validator("value")
    def check_length(cls, val: str, values: ValidationInfo):
        if val:
            min_length = values.data.get("min_length")
            max_length = values.data.get("max_length")
            if min_length is not None and len(val) < min_length:
                raise ValueError(
                    f"ensure this value has at least {min_length} characters"
                )
            if max_length is not None and len(val) > max_length:
                raise ValueError(
                    f"ensure this value has at most {max_length} characters"
                )
        return val


class ValidateStrongPassword(BaseModel):
    min_length: int = 8
    value: Union[str, None] = None

    @field_validator("value")
    def check_length(cls, val: str, values: ValidationInfo):
        if val:
            min_length = values.data.get("min_length")
            if len(val) < min_length:
                raise ValueError(
                    f"ensure this value has at least {min_length} characters"
                )

        if not is_valid_password(val):
            raise ValueError(
                f"ensure this value has at least {min_length} characters, one uppercase letter, one lowercase letter, one number and one special character."
            )

        return val
