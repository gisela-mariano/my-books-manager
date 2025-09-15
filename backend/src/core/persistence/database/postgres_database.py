import logging
import uuid
from asyncio import current_task
from contextlib import asynccontextmanager
from contextvars import ContextVar
from datetime import date, datetime, time
from typing import Any, Generator, List, Mapping, Optional, Type

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import Delete, Executable

logger = logging.getLogger("uvicorn.error")

transaction_current_session: ContextVar[Optional[AsyncSession]] = ContextVar(
    "transaction_current_session", default=None
)


class Database:
    def __init__(
        self,
        dsn: str,
        metadata: Type[DeclarativeBase],
        echo: bool = False,
    ) -> None:
        self.dsn = dsn
        self.metadata = metadata
        self.echo = echo

        self.async_postgresql_engine = create_async_engine(
            self.dsn,
            echo=echo,
        )

        self.async_postgresql_scoped_session_factory = async_scoped_session(
            async_sessionmaker(
                self.async_postgresql_engine,
                expire_on_commit=False,
                autoflush=False,
                autocommit=False,
                class_=AsyncSession,
            ),
            scopefunc=current_task,
        )

        logger.debug(f"Database connection established: {self.dsn}")

    async def initialize_postgres_db(self):
        async_engine = self.async_postgresql_engine
        metadata = self.metadata

        async with async_engine.begin() as connection:
            await connection.run_sync(metadata.create_all)

    async def close_postgres_db(self):
        """
        Fecha adequadamente a conexão com o PostgreSQL.
        Remove todas as sessões e dispõe do engine.
        """
        try:
            # Remove todas as sessões ativas
            await self.remove()

            # Fecha o engine do PostgreSQL
            await self.async_postgresql_engine.dispose()

            logger.debug("PostgreSQL connection closed successfully")
        except Exception as e:
            logger.error(f"Error while closing PostgreSQL connection: {e}")
            raise

    async def remove(self):
        # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#sqlalchemy.ext.asyncio.async_scoped_session.remove
        await self.async_postgresql_scoped_session_factory.remove()

    @asynccontextmanager
    async def session(
        self,
    ) -> Generator[AsyncSession, Any, None]:
        session: AsyncSession = self.async_postgresql_scoped_session_factory()
        try:
            logger.debug("AsyncSession created")
            yield session
        except Exception:
            logger.exception("AsyncSession rollback because of exception")
            await session.rollback()
            raise
        finally:
            logger.debug("Closing AsyncSession")
            await session.close()
            await self.remove()

    @asynccontextmanager
    async def transaction(
        self,
    ) -> Generator[AsyncSession, Any, None]:
        session: AsyncSession = self.async_postgresql_scoped_session_factory()

        try:
            logger.debug("Transaction created")
            async with session.begin():
                token = transaction_current_session.set(session)
                yield session
        except Exception:
            logger.exception("Transaction rollback because of exception")
            await session.rollback()
            raise
        finally:
            logger.debug("Closing Transaction")
            await session.close()
            transaction_current_session.reset(token)
            await self.remove()

    async def fetch_all(
        self, query: Executable, parameters: Optional[dict[str, Any]] = None
    ) -> List[dict[str, Any]]:
        session = transaction_current_session.get()

        async def execute(_session: AsyncSession):
            result = await _session.execute(query, parameters)
            fetch_all_result = result.mappings().fetchall()
            return (
                [self._serialize_row(row) for row in fetch_all_result]
                if fetch_all_result
                else []
            )

        if session is None:
            async with self.session() as session:
                result = await execute(session)
                await session.commit()
                return result
        else:
            return await execute(session)

    async def fetch_one(
        self, query: Executable, parameters: Optional[dict[str, Any]] = None
    ) -> dict[str, Any]:
        session = transaction_current_session.get()

        async def execute(_session: AsyncSession):
            result = await _session.execute(query, parameters)
            if query.is_delete is True:
                return {} if result.rowcount > 0 else None

            fetch_result = result.mappings().fetchone()
            return self._serialize_row(fetch_result) if fetch_result else {}

        if session is None:
            async with self.session() as session:
                result = await execute(session)
                await session.commit()
                return result
        else:
            return await execute(session)

    async def fetch_val(
        self, query: Executable, parameters: Optional[dict[str, Any]] = None
    ) -> Any:
        return await self.execute(query, parameters)

    async def execute(
        self, query: Executable, parameters: Optional[dict[str, Any]] = None
    ):
        session = transaction_current_session.get()

        async def execute(_session: AsyncSession):
            result = await _session.execute(query, parameters)
            if query.is_delete or query.is_update or query.is_insert:
                return result.rowcount
            else:
                return result.scalar()

        if session is None:
            async with self.session() as session:
                result = await execute(session)
                await session.commit()
                return result
        else:
            return await execute(session)

    async def delete(
        self, query: Delete, parameters: Optional[dict[str, Any]] = None
    ) -> bool:
        session = transaction_current_session.get()

        async def execute(_session: AsyncSession):
            result = await _session.execute(query, parameters)
            return result.rowcount > 0

        if session is None:
            async with self.session() as session:
                result = await execute(session)
                await session.commit()
                return result
        else:
            return await execute(session)

    def _serialize_row(self, row: Mapping[str, Any]) -> dict[str, Any]:
        """
        Serialize a single row, converting UUIDs, datetimes, and other non-JSON
        serializable types into JSON-compatible formats.
        """
        serialized: dict[str, Any] = {}
        for key, value in row.items():
            if isinstance(value, uuid.UUID):
                serialized[key] = str(value)
            elif isinstance(value, datetime):
                serialized[key] = value.isoformat()
            elif isinstance(value, date):
                serialized[key] = value.isoformat()
            elif isinstance(value, time):
                serialized[key] = value.isoformat()
            else:
                serialized[key] = value
        return serialized
