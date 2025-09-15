from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from src.core.utils.exceptions.errors import InputValidationError, RouteNotFoundError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_404_NOT_FOUND


async def http_validation_exception_handler(_: Request, exc: RequestValidationError):
    if exc.errors() and len(exc.errors()):
        for error in exc.errors():
            if "ctx" in error:
                del error["ctx"]

    raise InputValidationError("Input validation error", metadata=exc.errors())


async def http_exception_handler(_: Request, exc: StarletteHTTPException):
    if exc.status_code == HTTP_404_NOT_FOUND:
        raise RouteNotFoundError()
    raise Exception(exc.detail)


async def base_exception_handler(_: Request, exc):
    raise exc
