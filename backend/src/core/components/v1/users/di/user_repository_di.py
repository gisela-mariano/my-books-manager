from dependency_injector import containers, providers
from src.core.components.v1.users.infra.postgres_user_repository import (
    PostgresUserRepository,
)


class UserRepositoryDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()

    repository = providers.Factory(PostgresUserRepository, db=database_di.db)
