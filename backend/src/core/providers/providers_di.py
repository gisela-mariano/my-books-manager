from dependency_injector import containers, providers
from src.core.providers.google_books_api import GoogleBooksApiProvider


class ProvidersDI(containers.DeclarativeContainer):
    commons_di = providers.DependenciesContainer()

    google_books_api = providers.Singleton(GoogleBooksApiProvider)
