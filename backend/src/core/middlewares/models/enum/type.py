from enum import Enum


class ErrorType(str, Enum):
    SYSTEM = "system"
    BUSINESS = "business"
