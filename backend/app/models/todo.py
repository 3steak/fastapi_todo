from sqlalchemy import ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from app.db.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    archived: Mapped[bool] = mapped_column(Boolean, default=False)

    items: Mapped[List["TodoItem"]] = relationship(
        back_populates="todo", cascade="all, delete-orphan"
    )


class TodoItem(Base):
    __tablename__ = "todo_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    item_title: Mapped[str] = mapped_column(String, index=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    todo_id: Mapped[int] = mapped_column(ForeignKey("todos.id"))
    todo: Mapped["Todo"] = relationship(back_populates="items")
