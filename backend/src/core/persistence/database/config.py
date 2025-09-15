import logging
from os import environ
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from src.core.enums.database import DatabaseType

# Configuração geral
logger = logging.getLogger("uvicorn.error")
Base = declarative_base()
ECHO = environ.get("ECHO", "False").lower() == "true"
DATABASE_TYPE = environ.get("DATABASE_TYPE", DatabaseType.POSTGRES.value)
DATABASE_URI = environ.get("CONNECTION_STRING")
DATABASE_NAME = environ.get("DATABASE_NAME")


def normalize_uri(database_uri: str) -> str:
    if not isinstance(database_uri, str):
        raise TypeError(f"database_uri must be a string, got {type(database_uri)}")

    parsed_uri = urlparse(database_uri)
    query_params = parse_qs(parsed_uri.query)
    if "sslmode" in query_params:
        del query_params["sslmode"]

    if parsed_uri.scheme == "postgres":
        scheme = "postgresql+asyncpg"
    elif parsed_uri.scheme == "postgresql":
        scheme = "postgresql+asyncpg"
    else:
        scheme = parsed_uri.scheme

    normalized_uri = parsed_uri._replace(
        scheme=scheme, query=urlencode(query_params, doseq=True)
    )
    return urlunparse(normalized_uri)


if DATABASE_TYPE == DatabaseType.POSTGRES.value:
    if DATABASE_URI is not None:
        DATABASE_URI = normalize_uri(DATABASE_URI)
    else:
        logger.error("CONNECTION_STRING environment variable is not set")


def listen_for_database_events(container):
    """
    Adiciona listeners para eventos de banco de dados. Apenas para PostgreSQL.
    """
    if DATABASE_TYPE == DatabaseType.POSTGRES.value:
        if ECHO is True or logger.level == logging.DEBUG:

            @event.listens_for(
                container.db().async_postgresql_engine.sync_engine, "connect"
            )
            def connection_monitor(dbapi_connection, connection_record):
                message = "Nova conexão obtida do pool."
                logger.debug(f"\033[33m{message}\033[0m")

            @event.listens_for(
                container.db().async_postgresql_engine.sync_engine, "checkout"
            )
            def checkout_monitor(dbapi_connection, connection_record, connection_proxy):
                message = "Conexão emprestada do pool."
                logger.debug(f"\033[34m{message}\033[0m")
                logger.debug(
                    f"\033[34m{container.db().async_postgresql_engine.sync_engine.pool.status()}\033[0m"
                )


# Logs para depuração
logger.debug(f"Database type: {DATABASE_TYPE}")
logger.debug(f"Connection string: {DATABASE_URI}")
