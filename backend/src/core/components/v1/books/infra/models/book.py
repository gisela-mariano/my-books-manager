from sqlalchemy import ARRAY, TIMESTAMP, UUID, Column, SmallInteger, String, Table, text
from sqlalchemy.sql import func
from src.core.persistence.database.sqlalchemy import metadata

books = Table(
    "books",
    metadata,
    Column(
        name="id",
        type_=UUID,
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column(name="title", type_=String(length=255), nullable=False),
    Column(name="subtitle", type_=String(length=500)),
    Column(name="description", type_=String),
    Column(name="cover_url", type_=String(length=500)),
    Column(name="isbn_10", type_=String(length=10), unique=True),
    Column(name="isbn_13", type_=String(length=13), unique=True),
    Column(name="page_count", type_=SmallInteger),
    Column(name="published_date", type_=String(length=10)),
    Column(name="publisher", type_=String),
    Column(name="authors", type_=ARRAY(String)),
    Column(name="categories", type_=ARRAY(String)),
    Column(
        name="created_at", type_=TIMESTAMP, server_default=func.now(), nullable=False
    ),
    Column(name="updated_at", type_=TIMESTAMP, onupdate=func.now()),
)
