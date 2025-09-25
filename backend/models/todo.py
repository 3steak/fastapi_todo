from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List
from db.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, index=True)
    archived: Mapped[bool] = mapped_column(Boolean, default=False, index=True)

    # relations
    items : Mapped[list["TodoItem"]] = relationship(back_populates="todo", cascade="all, delete-orphan")


# ajout model todoitem
class TodoItem(Base):
    __tablename__ = 'todo_items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_title: Mapped[str] = mapped_column(String, index=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    # relations
    todo_id: Mapped[int] = mapped_column(ForeignKey("todos.id"))
    todo: Mapped["Todo"] = relationship(back_populates="items")



