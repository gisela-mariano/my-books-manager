import json
from datetime import datetime
from json.decoder import JSONDecodeError
from typing import Union, get_args, get_origin
from uuid import UUID

from pydantic import BaseModel


def alias_columns(table, alias_prefix: str):
    return tuple(
        [column.label(f"{alias_prefix}__{column.name}") for column in table.columns]
    )


def join_result_to_dict(
    class_model: type[BaseModel], result: dict, prefix: str, join_key: str
):
    result_dict = {join_key: {}}
    fields = class_model.model_fields

    for key, val in result.items():
        val = str(val) if isinstance(val, UUID) else val
        val = val.isoformat() if isinstance(val, datetime) else val

        if key.startswith(f"{prefix}__"):
            field_name = key.replace(f"{prefix}__", "")
            expected_field = fields.get(join_key).annotation
            expected_subfield = None

            if hasattr(expected_field, "model_fields"):
                expected_subfield = expected_field.model_fields.get(field_name)

            if expected_subfield and not _is_str_type(expected_subfield.annotation):
                try:
                    val = json.loads(val)
                except (JSONDecodeError, TypeError):
                    pass

            result_dict[join_key].setdefault(field_name, val)

        else:
            result_dict.setdefault(key, val)

    return class_model(**result_dict).model_dump(by_alias=True)


def _is_str_type(tp) -> bool:
    """
    Returns True if the expected type is str
    (considering Optional[str], Union[str, None], etc)
    """
    if tp is str:
        return True

    origin = get_origin(tp)
    if origin is Union:
        return any(_is_str_type(arg) for arg in get_args(tp))

    return False
