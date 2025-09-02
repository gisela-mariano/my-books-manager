class BaseException(Exception):
    def __init__(
        self,
        message,
        default_message,
        raised_error,
        code,
        error_type,
        acknowledge,
        metadata,
    ):
        self.message = message
        self.raised_error = raised_error
        self.default_message = default_message
        self.metadata = metadata
        self.acknowledge = acknowledge
        self.code = code
        self.type = error_type
