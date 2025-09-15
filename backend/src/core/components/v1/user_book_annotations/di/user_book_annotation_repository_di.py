from dependency_injector import containers, providers
from src.core.components.v1.user_book_annotations.infra.postgres_user_book_annotation_repository import (
    PostgresUserBookAnnotationRepository,
)


class UserBookAnnotationRepositoryDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()

    repository = providers.Factory(
        PostgresUserBookAnnotationRepository, db=database_di.db
    )
