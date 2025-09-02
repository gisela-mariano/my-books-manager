from dependency_injector import containers, providers


class ProvidersDI(containers.DeclarativeContainer):
    commons_di = providers.DependenciesContainer()
