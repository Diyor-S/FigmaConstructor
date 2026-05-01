from typing import Annotated, TYPE_CHECKING

from fastapi import Depends

from app.db import (
    db,
    Task
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class TaskManager:
    def __init__(self, session: "AsyncSession") -> None:
        self._session = session

    async def add(self, ):
        """
        Method to handle adding the task to the db

        :return: None
        """

    async def delete(self) -> None:
        """
        Method to delete the task from the db.
        Meaning the task will be deleted when it is done, or explicitly triggered the delete endpoint.

        :return: None
        """
        pass

    async def update(self) -> Task:
        pass

    async def get_by_name(self) -> Task:
        pass


def get_tasks_manager(session: Annotated["AsyncSession", Depends(db.get_session)]) -> TaskManager:
    return TaskManager(session=session)
