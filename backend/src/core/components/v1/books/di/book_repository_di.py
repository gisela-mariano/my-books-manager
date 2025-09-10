from dependency_injector import containers, providers
from src.core.components.v1.books.infra.postgres_book_repository import (
    PostgresBookRepository,
)


class BookRepositoryDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()

    repository = providers.Factory(PostgresBookRepository, db=database_di.db)
