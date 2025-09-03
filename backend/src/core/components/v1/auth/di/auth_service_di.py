from dependency_injector import containers, providers
from src.core.components.v1.auth.domain.auth_service import AuthService


class AuthServiceDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user_repository = providers.Dependency()

    service = providers.Factory(AuthService, user_repository=user_repository)
