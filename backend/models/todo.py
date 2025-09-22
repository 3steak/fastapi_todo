from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    archived = Column(Boolean, default=False, index=True)
    items = relationship("TodoItem", back_populates="todo", cascade="all, delete-orphan")

# ajout model todoitem
class TodoItem(Base):
        __tablename__ = 'todo_items'

        id = Column(Integer, primary_key=True, index=True)
        item_title = Column(String, index=True)
        completed = Column(Boolean, default=False, index=True)

        todo_id=  Column(Integer, ForeignKey("todos.id"))
        todo =  relationship("Todo", back_populates="items")



