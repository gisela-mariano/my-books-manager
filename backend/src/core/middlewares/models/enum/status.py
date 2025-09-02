from enum import Enum


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
