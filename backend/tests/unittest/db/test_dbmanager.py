import os
import unittest
from dotenv import load_dotenv

from pydantic import PostgresDsn
from sqlalchemy import make_url, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base, DBManager

load_dotenv(".env_tests")


class TestDBManager(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.url = PostgresDsn(os.getenv("DB_URL"))
        if not self.url:
            self.fail("DB_URl is missing from .env_tests")

        self.db = DBManager(
            url=str(self.url)
        )

        async with self.db.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def asyncTearDown(self):
        async with self.db.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
        await self.db.engine.dispose()

    async def test_db_init(self):
        self.assertEqual((str(self.url)), self.db.url.render_as_string(hide_password=False))
        self.assertEqual((
            make_url(self.db.url)).render_as_string(hide_password=False),
            self.db.engine.url.render_as_string(hide_password=False)
        )
        self.assertEqual(False, self.db.echo)

    async def test_session(self):
        async_generator_session = self.db.get_session()
        session = await anext(async_generator_session)

        try:
            self.assertIsInstance(session, AsyncSession)
            self.assertFalse(self.db.session_factory.kw.get("expire_on_commit"))
            result = (await session.execute(text("SELECT 1"))).scalar_one()

            self.assertEqual(result, 1)
        finally:
            await async_generator_session.aclose()

