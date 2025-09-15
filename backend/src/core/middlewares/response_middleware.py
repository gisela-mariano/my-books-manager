import json
import logging
from json import JSONDecodeError

from fastapi.responses import StreamingResponse
from src.core.middlewares.responses.error import (
    AuthUnauthorizedErrorResponse,
    InternalErrorResponse,
    RouteNotFoundErrorResponse,
    ValidationErrorResponse,
)
from src.core.middlewares.responses.success import SuccessResponse
from src.core.utils.exceptions.base_exception import BaseException
from src.core.utils.exceptions.errors import AuthUnauthorizedError, RouteNotFoundError
from starlette.middleware.base import BaseHTTPMiddleware


class ResponseMiddleware(BaseHTTPMiddleware):
    @staticmethod
    async def parse_response_body(response: StreamingResponse, request_route: str):
        raw_body = None
        async for body in response.body_iterator:
            try:
                raw_body = json.loads(body.decode("utf-8"))
            except JSONDecodeError as exc:
                raise JSONDecodeError(
                    msg=f"Failed to decode JSON. ResponseMiddleware expects to receive a valid JSON response in the route {request_route}",
                    doc=exc.doc,
                    pos=exc.pos,
                )

        return raw_body

    async def dispatch(self, request, call_next):
        doc_routes = ("/docs", "/redoc", "/openapi.json")
        try:
            response = await call_next(request)
            if request.url.path in doc_routes:
                return response

            raw_body = await self.parse_response_body(response, request.url.path)

            FASTAPI_UNPROCESSABLE_ENTITY_STATUS_CODE = 422
            if response.status_code == FASTAPI_UNPROCESSABLE_ENTITY_STATUS_CODE:
                raise Exception(raw_body)

            return SuccessResponse(content=raw_body)
        except RouteNotFoundError as exception:
            return RouteNotFoundErrorResponse(exception=exception)
        except AuthUnauthorizedError as exception:
            return AuthUnauthorizedErrorResponse(exception=exception)
        except BaseException as exception:
            return ValidationErrorResponse(exception=exception)
        except Exception as exception:
            logging.exception(msg=str(exception))
            return InternalErrorResponse(exception=exception)
