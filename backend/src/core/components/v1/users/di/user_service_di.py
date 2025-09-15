from dependency_injector import containers, providers
from src.core.components.v1.users.domain.user_service import UserService


class UserServiceDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    repository = providers.Dependency()

    service = providers.Factory(UserService, repository=repository)
