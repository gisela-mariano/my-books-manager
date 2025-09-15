from dependency_injector import containers, providers
from src.core.components.v1.books.domain.book_service import BookService


class BookServiceDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    repository = providers.Dependency()

    service = providers.Factory(BookService, repository=repository)
