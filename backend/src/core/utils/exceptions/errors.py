from src.core.middlewares.models.enum.type import ErrorType
from src.core.utils.exceptions.base_exception import BaseException


class ValidationPayloadError(BaseException):
    def __init__(
        self,
        message="Validation payload error",
        default_message="Validation payload error",
        raised_error="ValidationPayloadError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            code=1,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class DbError(BaseException):
    def __init__(
        self,
        message="Db with error",
        default_message="Db with error",
        raised_error="DbError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            code=2,
            error_type=ErrorType.SYSTEM.value,
            acknowledge=False,
            metadata=metadata,
        )


class AlreadyRegisteredError(BaseException):
    def __init__(
        self,
        message="Face already registered",
        default_message="Face already registered",
        raised_error="AlreadyRegisteredError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            code=3,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class InputValidationError(BaseException):
    def __init__(
        self,
        message="Input validation error",
        default_message="Input validation error",
        raised_error="InputValidationError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            code=4,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )


class RouteNotFoundError(BaseException):
    def __init__(
        self,
        message="Route not found",
        default_message="Route not found",
        raised_error="RouteNotFoundError",
        metadata=[],
    ):
        super().__init__(
            message=message,
            default_message=default_message,
            raised_error=raised_error,
            code=5,
            error_type=ErrorType.BUSINESS.value,
            acknowledge=True,
            metadata=metadata,
        )
