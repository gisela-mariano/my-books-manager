from typing import List

from pydantic import BaseModel
from src.core.middlewares.models.enum.type import ErrorType


class Error(BaseModel):
    message: str
    default_message: str = "unknown error occurred"
    raised_error: str = "UnknownException"
    type: ErrorType = ErrorType.SYSTEM
    metadata: List = []
    acknowledge: bool = True

    def __init__(self, exception):
        if not isinstance(exception, Exception) and not isinstance(exception, dict):
            raise AssertionError("Argument passed must be an Exception or a dict")

        # Do not have acknowledge as attr means that is a custom error
        if not hasattr(exception, "acknowledge") and not isinstance(exception, dict):
            exception.__setattr__(
                "message",
                "unknown error occurred with the following message: " + str(exception),
            )

        if isinstance(exception, Exception):
            super().__init__(**exception.__dict__)

        else:
            super().__init__(**exception)

    class Config:
        pass
