from sqlalchemy import (
    JSON,
    TIMESTAMP,
    UUID,
    Boolean,
    CheckConstraint,
    Column,
    Index,
    Integer,
    String,
    Table,
    text,
)
from sqlalchemy.sql import func
from src.core.persistence.database.sqlalchemy import metadata

users = Table(
    "users",
    metadata,
    Column(
        name="id",
        type_=UUID,
        primary_key=True,
        index=True,
        server_default=text("gen_random_uuid()"),
    ),
    Column(name="name", type_=String(length=255), nullable=False),
    Column(name="lastname", type_=String(length=255), nullable=False),
    Column(name="username", type_=String(length=255), nullable=False, unique=True),
    Column(name="email", type_=String(length=60), nullable=False, unique=True),
    Column(name="password", type_=String(length=255), nullable=False),
    Column(name="is_active", type_=Boolean, nullable=False, default=True),
    Column(
        name="created_at", type_=TIMESTAMP, server_default=func.now(), nullable=False
    ),
    Column(name="updated_at", type_=TIMESTAMP, onupdate=func.now()),
    Column(name="deleted_at", type_=TIMESTAMP),
)
