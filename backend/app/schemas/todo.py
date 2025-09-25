from pydantic import BaseModel
from typing import List

# ----- Items -----
class TodoItemBase(BaseModel):
    item_title: str

class TodoItemCreate(TodoItemBase):
    pass

class TodoItemSchema(TodoItemBase):
    id: int
    completed: bool

    class Config:
         from_attributes = True


# ----- Todos -----
class TodoBase(BaseModel):
    title: str

class TodoCreate(TodoBase):
    pass

class TodoSchema(TodoBase):
    id: int
    archived: bool
    items: List[TodoItemSchema] = []

    class Config:
         from_attributes = True
