import json
from datetime import datetime
from json.decoder import JSONDecodeError
from typing import Any, Union, get_args, get_origin
from uuid import UUID

from pydantic import BaseModel


def alias_columns(table, alias_prefix: str):
    return tuple(
        [column.label(f"{alias_prefix}__{column.name}") for column in table.columns]
    )


def join_result_to_dict(
    class_model: type[BaseModel], result: dict[str, Any]
) -> dict[str, Any]:
    """
    Converts the result of a SQLAlchemy join into a dict compatible with the Pydantic schema, supporting nested joins via multiple prefixes.

    The prefixes should represent the hierarchical path (separated by two underscores).

    For example, for the following schema:
    ```
    class Book(BaseModel):
       title: str

    class UserBook(BaseModel):
       user: str
       book: Book

    class UserBookNotes(BaseModel):
       note: str
       user_book: UserBook
    ```
    if I wanted to convert the dict to the representation of the `UserBookNotes` schema, the keys would have to come with the prefix `user_book__` for `UserBook` data and with the prefix `user_book__book__` for `Book` data.

    The SQLAlchemy query would be something like:
    ```
    j = join(
        user_book_notes,
        user_books,
        user_book_notes.c.user_book_id == user_books.c.id,
        full=True,)


    j_book = join(
        j,
        books,
        user_books.columns.book_id == books.columns.id,
        full=True,
    )

    query = (
        select(
            *user_book_notes.c,
            *alias_columns(user_books, “user_book”),
            *alias_columns(books, “user_book__book”)
        )
        .select_from(j_book)
        .where(user_book_notes.c.id == id))

    ```
    """
    result_dict: dict[str, Any] = {}
    fields = class_model.model_fields

    for key, val in result.items():
        val = str(val) if isinstance(val, UUID) else val
        val = val.isoformat() if isinstance(val, datetime) else val

        if "__" in key:
            path = key.split("__")
            field_name = path[-1]
            path_keys = path[:-1]

            current = result_dict
            for k in path_keys:
                if k not in current:
                    expected_field = fields.get(k)
                    if expected_field:
                        current[k] = {}
                    else:
                        current[k] = {}
                current = current[k]

            current[field_name] = val
        else:
            result_dict[key] = val

    return class_model(**result_dict).model_dump(by_alias=True)
