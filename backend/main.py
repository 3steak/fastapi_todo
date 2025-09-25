from fastapi import FastAPI
from typing import List

from test_db import create_tables, get_todos, add_todos, add_item
from models.schemas import TodoSchema, TodoCreate, TodoItemSchema, TodoItemCreate


app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Coucou"}

#GET toute les todos
@app.get("/todos", response_model=List[TodoSchema])
def list_todos():
    return get_todos()

# POST une nouvelle todolist
@app.post("/todos", response_model=TodoSchema)
def create_todo(todo : TodoCreate):
    return add_todos(todo.title)
    

# POST item dans todo existante
@app.post("/todos/{todo_id}/items", response_model=TodoItemSchema)
def create_todo_item(todo_id: int, item: TodoItemCreate):
    return add_item(todo_id, item.item_title)