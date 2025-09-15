from fastapi.responses import JSONResponse
from src.core.middlewares.models.enum.status import ResponseStatus
from src.core.middlewares.models.response import Response


class SuccessResponse(JSONResponse):
    def __init__(self, content: dict) -> None:
        body = Response(**dict(content), status=ResponseStatus.SUCCESS).model_dump()
        super().__init__(content=body)
