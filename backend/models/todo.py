from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional
from db.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title :Mapped[str]
    archived : Mapped[Optional[bool]]

    # relation
    items : Mapped[list["TodoItem"]] = relationship(back_populates="todo", cascade="all, delete-orphan")


# ajout model todoitem
class TodoItem(Base):
        __tablename__ = 'todo_items'

        id: Mapped[int] = mapped_column(Integer, primary_key=True)
        item_title :Mapped[str]
        completed : Mapped[Optional[bool]]

        todo_id : Mapped[int] =  mapped_column(ForeignKey("todos.id"))
        todo : Mapped["Todo"] =  relationship(back_populates="items")



