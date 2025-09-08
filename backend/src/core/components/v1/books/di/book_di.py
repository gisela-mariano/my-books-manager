from dependency_injector import containers, providers
from src.core.components.v1.books.application.use_cases.book_search import (
    BookSearchUseCase,
)


class BookDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    # Use cases
    book_search_use_case = providers.Factory(
        BookSearchUseCase, google_books_provider=providers_di.google_books_api
    )
