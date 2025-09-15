from dependency_injector import containers, providers
from src.core.components.v1.user_book_annotations.domain.user_book_annotation_service import (
    UserBookAnnotationService,
)


class UserBookAnnotationServiceDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    repository = providers.Dependency()

    service = providers.Factory(UserBookAnnotationService, repository=repository)
