from dependency_injector import containers, providers
from src.core.components.v1.auth.di.auth_service_di import AuthServiceDI


class AuthDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user_repository = providers.Dependency()

    _auth_service_di = providers.Container(
        AuthServiceDI, user_repository=user_repository
    )

    service = _auth_service_di().service
