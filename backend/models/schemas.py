from pydantic import BaseModel
from typing import List


class TodoItemSchema(BaseModel):
    id: int
    item_title: str
    completed: bool = False

    class Config:
        orm_mode = True


class TodoSchema(BaseModel):
    id: int
    title: str
    archived: bool = False
    items: List[TodoItemSchema] = []

    class Config:
        orm_mode = True


# schema pour la creation
class TodoCreate(BaseModel):
    title: str


class TodoItemCreate(BaseModel):
    item_title: str
