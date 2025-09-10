from sqlalchemy import (
    TIMESTAMP,
    UUID,
    Column,
    ForeignKeyConstraint,
    SmallInteger,
    String,
    Table,
    text,
)
from sqlalchemy.sql import func
from src.core.persistence.database.sqlalchemy import metadata

user_books = Table(
    "user_books",
    metadata,
    Column(
        name="id",
        type_=UUID,
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column(name="user_id", type_=UUID, index=True, nullable=False),
    Column(name="book_id", type_=UUID, index=True, nullable=False),
    Column(name="reading_status", type_=String(length=50)),
    Column(name="rating_star", type_=SmallInteger),
    Column(name="reading_start_date", type_=TIMESTAMP),
    Column(name="reading_end_date", type_=TIMESTAMP),
    Column(
        name="created_at", type_=TIMESTAMP, server_default=func.now(), nullable=False
    ),
    Column(name="updated_at", type_=TIMESTAMP, onupdate=func.now()),
    ForeignKeyConstraint(
        ["user_id"],
        ["users.id"],
        name="fk_user_books_user_id",
    ),
    ForeignKeyConstraint(
        ["book_id"],
        ["books.id"],
        name="fk_user_books_book_id",
    ),
)
