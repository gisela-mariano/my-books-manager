from dependency_injector import containers, providers
from src.core.components.v1.user_books.infra.postgres_user_book_repository import (
    PostgresUserBookRepository,
)


class UserBookRepositoryDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()

    repository = providers.Factory(PostgresUserBookRepository, db=database_di.db)
