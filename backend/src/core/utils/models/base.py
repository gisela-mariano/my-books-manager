import inspect
from typing import Union

from pydantic import BaseModel, Field
from pydantic._internal._model_construction import ModelMetaclass


def convert_str_to_camel_case(snake_str: str):
    first_word, *others = snake_str.split("_")
    return "".join([first_word.lower(), *map(str.title, others)])


class BaseConfig:
    alias_generator = convert_str_to_camel_case
    validate_by_name = True
    use_enum_values = True
    str_min_length = 0


class BaseInDb(BaseModel):
    id: str
    created_at: str
    updated_at: Union[str, None] = Field(default=None)
    deleted_at: Union[str, None] = Field(default=None)

    class Config(BaseConfig):
        pass


class AllOptional(ModelMetaclass):
    def __new__(cls, name, bases, namespaces, **kwargs):
        annotations = namespaces.get("__annotations__", {})
        for base in bases:
            annotations.update(base.__annotations__)
        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Union[annotations[field], None]
        namespaces["__annotations__"] = annotations
        return super().__new__(cls, name, bases, namespaces, **kwargs)


def exclude_fields(*fields):
    def dec(_cls):
        for field in fields:
            if field in _cls.model_fields:
                del _cls.model_fields[field]

        _cls.model_rebuild(force=True)
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.model_fields
        return dec(cls)
    return dec
