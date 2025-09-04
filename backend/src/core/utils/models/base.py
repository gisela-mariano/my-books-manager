import inspect
from typing import Callable, Optional, Type, TypeVar, Union, get_origin

from pydantic import BaseModel, ConfigDict, Field
from pydantic._internal._model_construction import ModelMetaclass

TModel = TypeVar("TModel", bound=BaseModel)


def convert_str_to_camel_case(snake_str: str):
    first_word, *others = snake_str.split("_")
    return "".join([first_word.lower(), *map(str.title, others)])


class BaseConfig(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True,
        use_enum_values=True,
        str_min_length=0,
        alias_generator=convert_str_to_camel_case,
    )


class BaseInDb(BaseConfig):
    id: str
    created_at: str
    updated_at: Union[str, None] = Field(default=None)
    deleted_at: Union[str, None] = Field(default=None)


class AllOptional(ModelMetaclass):

    def __new__(mcs, name, bases, namespace, **kwargs):
        new_annotations = {}

        # Set inherited fields as optional
        for base in bases:
            if issubclass(base, BaseModel):
                for field_name, field_info in base.model_fields.items():
                    field_type = field_info.annotation

                    if not get_origin(field_type) is Optional:
                        new_annotations[field_name] = Optional[field_type]

                    namespace.setdefault(field_name, None)

        # Set class fields as optional
        annotations = namespace.get("__annotations__", {})
        for field_name, field_type in annotations.items():

            if not get_origin(field_type) is Optional:
                new_annotations[field_name] = Optional[field_type]

            namespace.setdefault(field_name, None)

        namespace["__annotations__"] = new_annotations
        return super().__new__(mcs, name, bases, namespace, **kwargs)


def exclude_fields(*fields):
    """
    Decorator to exclude fields from a Pydantic model.

    Args:
        *fields: The names of the fields to exclude.

    Returns:
        A decorator that modifies the Pydantic model.
    """

    def decorator(_cls):
        for field in fields:
            if field in _cls.model_fields:
                del _cls.model_fields[field]

        _cls.model_rebuild(force=True)
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], BaseModel):
        cls = fields[0]
        fields = cls.model_fields
        return decorator(cls)
    return decorator


def remove_validators(
    *validators_to_remove: str,
) -> Callable[[Type[TModel]], Type[TModel]]:
    """
    Decorator to remove validators from a Pydantic model.

    This is useful when inheriting from a model and wanting to remove
    a validator from the parent class in the child class.

    Args:
        *validators_to_remove: The names of the validator methods to remove.

    Returns:
        A decorator that modifies the Pydantic model.
    """

    def decorator(cls: Type[TModel]) -> Type[TModel]:
        if not hasattr(cls, "__pydantic_decorators__"):
            return cls

        validators = cls.__pydantic_decorators__.field_validators.copy()

        for validator_name in validators_to_remove:
            if validator_name in validators:
                del validators[validator_name]

        cls.__pydantic_decorators__.field_validators = validators
        cls.model_rebuild(force=True)
        return cls

    return decorator
