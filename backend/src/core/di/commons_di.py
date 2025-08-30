from dependency_injector import containers, providers

from src.core.persistence.utils.settings import Settings


class SettingsConfig(Settings):
    """Configurações de ambiente."""

    def __init__(self):
        super().__init__()
        self.set_env("./config/environment.yaml")


class CommonsDI(containers.DeclarativeContainer):

    env_settings = providers.Singleton(SettingsConfig)
