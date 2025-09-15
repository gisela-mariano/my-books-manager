from dependency_injector import containers, providers
from src.core.components.components_di import ComponentsDI
from src.core.di.commons_di import CommonsDI
from src.core.enums.database import DatabaseType
from src.core.persistence.database.config import DATABASE_TYPE
from src.core.persistence.database.database_di import DatabaseDI
from src.core.providers.providers_di import ProvidersDI


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["src.api.v1.routes"])

    # Dependencias
    commons_di = providers.Container(CommonsDI)

    database_di = providers.Container(DatabaseDI)

    db = None
    db_engine = None
    db_session = None

    if DATABASE_TYPE == DatabaseType.POSTGRES.value:
        db = database_di.db
        db_engine = database_di.db_engine
        db_session = database_di.db_session

    providers_di = providers.Container(
        ProvidersDI,
        commons_di=commons_di,
    )

    components = providers.Container(
        ComponentsDI,
        database_di=database_di,
        commons_di=commons_di,
        providers_di=providers_di,
    )
