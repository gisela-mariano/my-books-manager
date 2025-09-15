from sqlalchemy import (
    TIMESTAMP,
    UUID,
    Column,
    ForeignKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.sql import func
from src.core.persistence.database.sqlalchemy import metadata

user_book_annotations = Table(
    "user_book_annotations",
    metadata,
    Column(
        name="id",
        type_=UUID,
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column(name="user_book_id", type_=UUID, index=True, nullable=False),
    Column(name="note", type_=String),
    Column(
        name="created_at", type_=TIMESTAMP, server_default=func.now(), nullable=False
    ),
    Column(name="updated_at", type_=TIMESTAMP, onupdate=func.now()),
    ForeignKeyConstraint(
        ["user_book_id"],
        ["user_books.id"],
        name="fk_user_book_annotations_user_book_id",
    ),
)
