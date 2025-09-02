from dependency_injector import containers, providers
from src.core.components.v1.users.application.use_cases.user_creation_use_case import (
    UserCreationUseCase,
)
from src.core.components.v1.users.di.user_repository_di import UserRepositoryDI


class UserDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    _user_repository_di = providers.Container(UserRepositoryDI, database_di=database_di)

    repository = _user_repository_di().repository

    # Use cases
    user_creation_use_case = providers.Factory(
        UserCreationUseCase, repository=repository
    )
