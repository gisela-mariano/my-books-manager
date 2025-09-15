from typing import List, Union

from sqlalchemy import Table, delete, insert, select, update
from src.core.persistence.database.postgres_database import Database as PostgresDatabase


class PostgresBaseRepository:

    def __init__(self, db: PostgresDatabase):
        self.db = db

    async def create_data(self, table: Table, payload: dict) -> dict:
        query = insert(table).returning(*table.columns).values(**payload)
        result = await self.db.fetch_one(query)

        return result

    async def get_data_by_id(self, table: Table, id: str) -> dict:
        query = select(table).where(
            table.c.id == id,
        )
        result = await self.db.fetch_one(query)

        return result

    async def get_data_by_specific_column(
        self, table: Table, column: str, value: Union[str, int, bool]
    ) -> dict:
        query = select(table).where(
            table.columns[column] == value,
        )
        result = await self.db.fetch_one(query)

        return result

    async def get_data_list_by_specific_column(
        self, table: Table, column: str, value: Union[str, int, bool]
    ) -> List[dict]:
        query = select(table).where(
            table.columns[column] == value,
        )
        result = await self.db.fetch_all(query)

        return result

    async def update_data(self, table: Table, payload: dict, id: str) -> dict:
        query = (
            update(table)
            .returning(*table.columns)
            .where(table.c.id == id)
            .values(payload)
        )
        result = await self.db.fetch_one(query)

        return result

    async def delete_data(self, table: Table, id: str) -> bool:
        query = delete(table).where(table.c.id == id)

        result = await self.db.delete(query)

        return result
