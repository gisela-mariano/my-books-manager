import inspect


def create_error_metadata(error: str, payload: dict, where: str, from_: dict) -> dict:
    return {
        "exception": error,
        "payload": payload,
        "where": where,
        "from": from_,
    }


def get_caller_info(depth=2) -> dict:
    """This function will return data from the function that is calling a particular function

    Args:
        depth (int, optional): This is the level of depth of the function from which the data should be sought. For example, the service calls the repository and the repository calls this function (get_caller_info), if the depth was 1 the information returned would be from the repository, but as I want the information from the service the depth is 2. Defaults to 2.

    Returns:
        {
          "function": str or None
          "line": str or None
          "context": str or None
          "class": str or None
        }
    """

    origin = inspect.stack()[depth]
    return {
        "function": origin.function or None,
        "line": origin.lineno or None,
        "context": (
            origin.code_context[0]
            if origin.code_context and len(origin.code_context) > 0
            else None
        ),
        "class": (
            origin.frame.f_locals.get("self").__class__.__name__
            if "self" in origin.frame.f_locals
            else None
        ),
    }


def get_caller_payload() -> dict:
    """This function will return a dictionary with the parameters of the function that is calling it."""

    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)

    return {arg: values[arg] for arg in args if arg != "self"}


def get_caller_name() -> str:
    """This function will return the name of the function that is calling it, including the class name if applicable."""

    frame = inspect.currentframe().f_back
    function_name = frame.f_code.co_name

    class_name = (
        frame.f_locals.get("self", None).__class__.__name__
        if "self" in frame.f_locals
        else None
    )

    if class_name:
        return f"{class_name}.{function_name}"

    return function_name
