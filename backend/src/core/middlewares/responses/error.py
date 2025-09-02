from abc import ABC

from fastapi.responses import JSONResponse
from src.core.middlewares.models.enum.status import ResponseStatus
from src.core.middlewares.models.error import Error
from src.core.middlewares.models.response import Response
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)


class BaseErrorResponse(JSONResponse, ABC):
    _status_code: str
    _default_message: str
    _code: str

    def __init__(self, exception: Exception) -> None:
        content_formatted = self.format_content(exception)
        super().__init__(content=content_formatted, status_code=self._status_code)

    @staticmethod
    def format_content(exception: Exception):
        error = Error(exception=exception)
        error.Config.use_enum_values = True
        return Response(
            **dict(
                data=None,
                message=error.message or error.default_message,
                error=error,
                status=ResponseStatus.FAILED,
                metadata=error.metadata,
            )
        ).model_dump()


class InternalErrorResponse(BaseErrorResponse):
    _status_code = HTTP_500_INTERNAL_SERVER_ERROR
    _default_message = "Unexpected error"
    _code = 1


class ValidationErrorResponse(BaseErrorResponse):
    _status_code = HTTP_400_BAD_REQUEST


class RouteNotFoundErrorResponse(BaseErrorResponse):
    _status_code = HTTP_404_NOT_FOUND
