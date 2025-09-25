from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import Base, engine, get_sessiondep
from app.schemas.todo import TodoSchema, TodoCreate, TodoItemSchema, TodoItemCreate
from app.crud import todo as crud
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Crée les tables
Base.metadata.create_all(bind=engine)

# ----- Hello -----
@app.get("/")
def root():
    return {"message": "Bienvenue sur API Todo"}


# ----- Todos -----
@app.get("/todos", response_model=List[TodoSchema])
def list_todos(session: Session = Depends(get_sessiondep)):
    return crud.get_todos(session)

@app.post("/todos", response_model=TodoSchema, status_code=201)
def create_todo(todo: TodoCreate, session: Session = Depends(get_sessiondep)):
    return crud.create_todo(session, todo)

@app.get("/todos/{todo_id}", response_model=TodoSchema)
def get_todo(todo_id: int, session: Session = Depends(get_sessiondep)):
    db_todo = crud.get_todo(session, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.patch("/todos/{todo_id}", response_model=TodoSchema)
def toggle_todo(todo_id: int, session: Session = Depends(get_sessiondep)):
    db_todo = crud.toggle_todo_archived(session, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, session: Session = Depends(get_sessiondep)):
    db_todo = crud.delete_todo(session, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None


# ----- Items -----
@app.post("/todos/{todo_id}/items", response_model=TodoItemSchema, status_code=201)
def add_item(todo_id: int, item: TodoItemCreate, session: Session = Depends(get_sessiondep)):
    db_item = crud.add_item(session, todo_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_item

@app.patch("/items/{item_id}", response_model=TodoItemSchema)
def toggle_item(item_id: int, session: Session = Depends(get_sessiondep)):
    db_item = crud.toggle_item_completed(session, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, session: Session = Depends(get_sessiondep)):
    db_item = crud.delete_item(session, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return None
