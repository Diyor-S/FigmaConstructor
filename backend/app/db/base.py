from typing import TYPE_CHECKING

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from validators import AsyncURLValidator

if TYPE_CHECKING:
    from sqlalchemy import URL
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class Base(DeclarativeBase):
    pass


class DBManager:
    url: AsyncURLValidator = AsyncURLValidator()

    def __init__(self, url: str) -> None:
        self.url: "URL" = url
        self.engine: "AsyncEngine" = create_async_engine(self.url)

    async def session_factory(self):
        pass

    async def get_session(self):
        pass
