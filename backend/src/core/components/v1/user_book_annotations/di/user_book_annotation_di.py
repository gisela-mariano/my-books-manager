from dependency_injector import containers, providers
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_create_use_case import (
    UseBookAnnotationCreateUseCase,
)
from src.core.components.v1.user_book_annotations.application.use_cases.user_book_annotation_get_by_id_user_case import (
    UserBookAnnotationGetByIdUseCase,
)
from src.core.components.v1.user_book_annotations.di.user_book_annotation_repository_di import (
    UserBookAnnotationRepositoryDI,
)
from src.core.components.v1.user_book_annotations.di.user_book_annotation_service_di import (
    UserBookAnnotationServiceDI,
)


class UserBookAnnotationDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user_book_service = providers.Dependency()

    _user_book_annotation_repository_di = providers.Container(
        UserBookAnnotationRepositoryDI, database_di=database_di
    )

    repository = _user_book_annotation_repository_di().repository

    _user_book_annotation_service_di = providers.Container(
        UserBookAnnotationServiceDI, repository=repository
    )

    service = _user_book_annotation_service_di().service

    # Use cases
    user_book_annotation_create_use_case = providers.Factory(
        UseBookAnnotationCreateUseCase,
        repository=repository,
        user_book_service=user_book_service,
    )

    user_book_annotation_get_by_id_user_case = providers.Factory(
        UserBookAnnotationGetByIdUseCase,
        repository=repository,
    )
