from typing import TYPE_CHECKING

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from validators import AsyncURLValidator
from core.config import settings

if TYPE_CHECKING:
    from typing import AsyncGenerator

    from sqlalchemy import URL
    from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession


class Base(DeclarativeBase):
    pass


class DBManager:
    url: AsyncURLValidator = AsyncURLValidator()

    def __init__(self, url: str, echo: bool = False) -> None:
        self.url: "URL" = url
        self.echo: bool = echo
        self.engine: "AsyncEngine" = create_async_engine(self.url)
        self.session_factory: async_sessionmaker["AsyncSession"] = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

    async def get_session(self) -> "AsyncGenerator[AsyncSession, None]":
        async with self.session_factory() as session:
            yield session

db = DBManager(
    url=str(settings.db.url),
    echo=settings.db.echo,
)