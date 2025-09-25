from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from db.database import get_sessiondep
from test_db import create_tables, get_todos, add_todos, add_item
from models.schemas import TodoSchema, TodoCreate, TodoItemSchema, TodoItemCreate

from db.database import Base, engine, SessionLocal
from models.todo import Todo, TodoItem

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Coucou"}

#GET toute les todos
@app.get("/todos", response_model=List[TodoSchema])
def list_todos(session : Session = Depends(get_sessiondep)):
    return get_todos(session)

# POST une nouvelle todolist
@app.post("/todos", response_model=TodoSchema)
def create_todo(todo : TodoCreate, session : Session = Depends(get_sessiondep)):
    return add_todos(todo.title, session)
    

# POST item dans todo existante
@app.post("/todos/{todo_id}/items", response_model=TodoItemSchema)
def create_todo_item(todo_id: int, item: TodoItemCreate, session : Session = Depends(get_sessiondep)):
    return add_item(todo_id, item.item_title, session)

#  PUT todolist archived
# PUT item completed