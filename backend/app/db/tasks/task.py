from typing import List, Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import String, ForeignKey

from app.db.base import Base
from app.db.mixins import IntIdMixin
from .status import TaskStatus


class Task(IntIdMixin, Base):
    """
    Task class , the purpose of it, the task has the status to show whether
    it is pending , done or in review or something else.

    task should have a name so user can understand which tasks it is doing, 

    the task should have a short description defining what to do exactly. what the task is about.

    Considering the fact that we can create a sub task for some task, many sub tasks to one main task
    We should have relationship many to one, or one to many. I guess bidirectional relationship
    at the application level, while on the database we can have one-to-many

    So how exactly am I gonna implement the relationship?
    What tools we have?

    We need Foreignkey() for relationship at the database level
    We need relationship() for relationship at the application level.
    """
    __tablename__ = "tasks"

    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey("tasks.id"))
    parent_task: Mapped["Task"] = relationship(back_populates="sub_tasks", remote_side=lambda: Task.id)

    status: Mapped[SQLAlchemyEnum] = mapped_column(SQLAlchemyEnum(TaskStatus), default=TaskStatus.TODO, nullable=False)

    name: Mapped[str] = mapped_column(String(30))
    short_description: Mapped[str] = mapped_column(String(30))
    
    sub_tasks: Mapped[List["Task"]] = relationship(back_populates="parent_task") 