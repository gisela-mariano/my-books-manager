from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field, ValidationInfo, field_validator
from src.core.middlewares.models.enum.status import ResponseStatus
from src.core.middlewares.models.error import Error


class Response(BaseModel):

    status_code: Optional[int] = Field(400, ge=200, le=599, exclude=True)
    status: ResponseStatus = ResponseStatus.FAILED
    message: str = "unknown error occurred"
    data: Any = None
    error: Union[Error, None] = None
    metadata: List = []

    def __init__(self, **kwargs):
        if isinstance(kwargs.get("error"), dict):
            kwargs["error"] = Error(kwargs["error"])
        super().__init__(**kwargs)

    @field_validator("status_code")
    def set_status_code(cls, status_code):
        return status_code or 400

    @field_validator("status")
    def set_status(cls, status, values: ValidationInfo):
        if "status_code" not in values.data.keys():
            return ResponseStatus.FAILED
        return (
            ResponseStatus.SUCCESS
            if str(values.data.get("status_code")).startswith("2")
            else ResponseStatus.FAILED
        )

    @field_validator("message")
    def check_status(cls, message, values: ValidationInfo):
        if (
            values.data.get("status") == ResponseStatus.SUCCESS
            and message == "unknown error occurred"
        ):
            raise AssertionError("If status is 'success' message should NOT be default")
        return message

    @field_validator("error")
    def check_error(cls, error, values: ValidationInfo):
        if values.data.get("status") == ResponseStatus.SUCCESS and error is not None:
            raise AssertionError(
                "if status is 'success', error should be None OR if error is not None, status should be 'failed'"
            )
        if values.data.get("status") == ResponseStatus.FAILED and error is None:
            raise AssertionError("if status is 'failed', error should NOT be None")
        return error
