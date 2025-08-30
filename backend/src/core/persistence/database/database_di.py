from dependency_injector import containers, providers

from src.core.persistence.database.postgres_database import Database as PostgresDatabase
from src.core.enums.database import DatabaseType
from src.core.persistence.database.config import DATABASE_TYPE, DATABASE_URI, ECHO, Base

class DatabaseDI(containers.DeclarativeContainer):
    db = None
    db_engine = None
    db_session = None

    if DATABASE_TYPE == DatabaseType.POSTGRES.value:
        db = providers.Singleton(
            PostgresDatabase,
            dsn=DATABASE_URI,
            echo=ECHO,
            metadata=Base.metadata
        )

        db_engine = db.provided.async_postgresql_engine
        db_session = providers.Factory(db.provided.session)