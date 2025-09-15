from dependency_injector import containers, providers
from src.core.components.v1.user_books.domain.user_book_service import UserBookService


class UserBookServiceDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    repository = providers.Dependency()

    service = providers.Factory(UserBookService, repository=repository)
