from dependency_injector import containers, providers
from src.core.components.v1.users.di.user_di import UserDI
from src.core.components.v1.users.di.user_repository_di import UserRepositoryDI


class ComponentsDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user = providers.Container(
        UserDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
    )
