from typing import Any
from uuid import uuid4

from pydantic import create_model


def get_responses(model):
    """Get standardized responses

    Args:
        model (class): Generic model


    Returns:
        dict: responses with their respective codes
    """

    success = f"Success {uuid4()}"
    bad_request = f"Bad Request {uuid4()}"
    internal_server_error = f"Internal Server Error {uuid4()}"

    error = {
        "message": "string",
        "default_message": "unknown error occurred",
        "raised_error": "UnknownException",
        "type": "system",
        "code": 1,
        "metadata": [],
        "acknowledge": True,
    }

    return {
        200: {
            "model": create_model(
                success,
                data=(model, ...),
                error=(Any, {}),
                status_code=(int, 200),
                message=(str, "success"),
                status=(str, "success"),
            )
        },
        400: {
            "model": create_model(
                bad_request,
                data=(Any, {}),
                error=(Any, error),
                status_code=(int, 400),
                message=(str, "unknown error occurred"),
            )
        },
        500: {
            "model": create_model(
                internal_server_error,
                data=(Any, {}),
                error=(Any, error),
                status_code=(int, 500),
                message=(str, "unknown error occurred"),
            )
        },
    }
