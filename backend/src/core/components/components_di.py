from dependency_injector import containers, providers
from src.core.components.v1.auth.di.auth_di import AuthDI
from src.core.components.v1.books.di.book_di import BookDI
from src.core.components.v1.user_books.di.user_book_di import UserBookDI
from src.core.components.v1.users.di.user_di import UserDI
from src.core.components.v1.users.di.user_repository_di import UserRepositoryDI


class CrossModuleDependenciesDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    user_repository = providers.Container(UserRepositoryDI, database_di=database_di)


class ComponentsDI(containers.DeclarativeContainer):
    database_di = providers.DependenciesContainer()
    commons_di = providers.DependenciesContainer()
    providers_di = providers.DependenciesContainer()

    _cross_dependencies = providers.Container(
        CrossModuleDependenciesDI,
        database_di=database_di,
        providers_di=providers_di,
    )

    auth = providers.Container(
        AuthDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
        user_repository=_cross_dependencies.user_repository.repository,
    )

    user = providers.Container(
        UserDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
        auth_service=auth.service,
    )

    book = providers.Container(
        BookDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
    )

    user_book = providers.Container(
        UserBookDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
        user_service=user.service,
        book_service=book.service,
    )
