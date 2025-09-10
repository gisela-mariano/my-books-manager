from dependency_injector import containers, providers
from src.core.components.v1.books.application.use_cases.book_search import (
    BookSearchUseCase,
)
from src.core.components.v1.books.di.book_repository_di import BookRepositoryDI
from src.core.components.v1.books.di.book_service_di import BookServiceDI


class BookDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    _book_repository_di = providers.Container(BookRepositoryDI, database_di=database_di)

    repository = _book_repository_di().repository

    _book_service_di = providers.Container(BookServiceDI, repository=repository)

    service = _book_service_di().service

    # Use cases
    book_search_use_case = providers.Factory(
        BookSearchUseCase, google_books_provider=providers_di.google_books_api
    )
