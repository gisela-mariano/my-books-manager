from dependency_injector import containers, providers
from src.core.components.v1.user_books.application.use_cases.user_book_create_use_case import (
    UserBookCreateUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_get_by_id_use_case import (
    UserBookGetByIdUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_get_user_books import (
    UserBookGetUserBooksUseCase,
)
from src.core.components.v1.user_books.application.use_cases.user_book_update_use_case import (
    UserBookUpdateUseCase,
)
from src.core.components.v1.user_books.di.user_book_repository_di import (
    UserBookRepositoryDI,
)
from src.core.components.v1.user_books.di.user_book_service_di import UserBookServiceDI


class UserBookDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user_service = providers.Dependency()
    book_service = providers.Dependency()

    _user_book_repository_di = providers.Container(
        UserBookRepositoryDI, database_di=database_di
    )

    repository = _user_book_repository_di().repository

    _user_book_service_di = providers.Container(
        UserBookServiceDI, repository=repository
    )

    service = _user_book_service_di().service

    # Use cases
    user_book_create_use_case = providers.Factory(
        UserBookCreateUseCase,
        repository=repository,
        service=service,
        book_service=book_service,
        user_service=user_service,
    )

    user_book_get_user_books_use_case = providers.Factory(
        UserBookGetUserBooksUseCase,
        repository=repository,
        user_service=user_service,
    )

    user_book_get_by_id_use_case = providers.Factory(
        UserBookGetByIdUseCase,
        repository=repository,
    )

    user_book_update_use_case = providers.Factory(
        UserBookUpdateUseCase,
        repository=repository,
        service=service,
    )
