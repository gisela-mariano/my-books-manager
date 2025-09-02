from typing import Any, Optional, Union

from pydantic import BaseModel, Field, model_validator
from src.core.middlewares.models.error import Error


class BaseResponse(BaseModel):
    status_code: Optional[int] = Field(200, ge=200, le=599)
    message: str = ""
    data: Any = None
    error: Union[Error, None] = None

    class Config:
        validate_assignment = True

    @model_validator(mode="before")
    def set_status_code(cls, values: dict):
        if values.get("error") is not None:
            values["status_code"] = 400
        return values
