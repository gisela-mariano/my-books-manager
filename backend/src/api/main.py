import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.router import routes as api_v1_routes
from src.core.di.containers import Container
from src.core.enums.database import DatabaseType
from src.core.middlewares.response_middleware import ResponseMiddleware
from src.core.utils.exceptions.base_exception import BaseException
from src.core.utils.exceptions.handlers import (
    base_exception_handler,
    http_exception_handler,
    http_validation_exception_handler,
)
from starlette.exceptions import HTTPException as StarletteHTTPException

# DI-1: Inicia o container
container = Container()

# DI-2: Inicia os recursos
container.init_resources()


@asynccontextmanager
async def lifespan(app: FastAPI):
    database_type = os.environ.get("DATABASE_TYPE")

    if database_type == DatabaseType.POSTGRES.value:
        # Inicialização do postgres
        db_instance = container.database_di.db()

        try:
            await db_instance.initialize_postgres_db()
            print("PostgreSQL connection established")
        except Exception as e:
            print(f"Error while connecting to PostgreSQL: {e}")
            raise
    else:
        raise ValueError(f"Unsupported DATABASE_TYPE: {database_type}")

    # DI-3: Verifica as dependencias
    container.check_dependencies()

    yield

    if database_type == DatabaseType.POSTGRES.value:
        # Fecha a conexão com o Postgres (se necessário)
        db_instance = container.database_di.db()
        await db_instance.close_postgres_db()
        print("PostgreSQL connection closed")


app = FastAPI(lifespan=lifespan)

app.include_router(api_v1_routes)

# Exception Handlers
app.add_exception_handler(RequestValidationError, http_validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(BaseException, base_exception_handler)

# Middlewares
app.add_middleware(ResponseMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
