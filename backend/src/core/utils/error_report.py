import inspect
from typing import Any, Dict


def get_caller_info(depth: int = 2) -> Dict[str, Any]:
    """This function will return data from the function that is calling a particular function.

    Args:
        depth (int, optional): How deep (in the sense of child to parent) in the hierarchy must one go to obtain the function data. Defaults to 2.

            - depth=0: That would be that function itself (where inspect.stack() was called)
            - depth=1: Would be the immediate caller
            - depth=2: Would be the caller of the caller
            ...

    Returns:
        {
          "function": Optional[str]
          "line": Optional[str]
          "context": Optional[str]
          "class": Optional[str]
        }
    """

    origin = inspect.stack()[depth]
    return {
        "function": origin.function or None,
        "line": origin.lineno or None,
        "context": (
            origin.code_context[0].strip()
            if origin.code_context and len(origin.code_context) > 0
            else None
        ),
        "class": (
            origin.frame.f_locals.get("self").__class__.__name__
            if "self" in origin.frame.f_locals
            else None
        ),
    }


def get_caller_payload(depth: int = 2) -> Dict[str, Any]:
    """This function will return a dictionary with the parameters (args) of the function that is calling it.

    Args:
        depth (int, optional): How deep (in the sense of child to parent) in the hierarchy must one go to obtain the function data. Defaults to 2.

            - depth=0: That would be that function itself (where inspect.stack() was called)
            - depth=1: Would be the immediate caller
            - depth=2: Would be the caller of the caller
            ...
    """

    origin = inspect.stack()[depth]
    frame = origin.frame
    args, _, _, values = inspect.getargvalues(frame)
    return {arg: values[arg] for arg in args if arg != "self"}


def get_caller_name(depth: int = 2) -> str:
    """This function will return the name of the function that is calling it, including the class name if applicable.

    Args:
        depth (int, optional): How deep (in the sense of child to parent) in the hierarchy must one go to obtain the function data. Defaults to 2.

            - depth=0: That would be that function itself (where inspect.stack() was called)
            - depth=1: Would be the immediate caller
            - depth=2: Would be the caller of the caller
            ...
    """

    origin = inspect.stack()[depth]
    frame = origin.frame
    function_name = frame.f_code.co_name
    class_name = (
        frame.f_locals.get("self").__class__.__name__
        if "self" in frame.f_locals
        else None
    )

    if class_name:
        return f"{class_name}.{function_name}"

    return function_name


def get_exception_metadata(e: Exception, depth: int = 2) -> dict:
    """
    depth (int, optional): This is the level of depth of the function from which the data should be sought. For example, the service calls the repository and the repository calls this function (get_caller_info), if the depth was 1 the information returned would be from the repository, but as I want the information from the service the depth is 2. Defaults to 2.
    """
    return {
        "exception": str(e),
        "payload": get_caller_payload(depth=depth),
        "where": get_caller_name(depth=depth),
        "from": get_caller_info(depth=depth + 1),
    }
