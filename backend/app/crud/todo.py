from sqlalchemy.orm import Session
from app.models.todo import Todo, TodoItem
from app.schemas.todo import TodoCreate, TodoItemCreate
from sqlalchemy.orm import Session, joinedload


# ----- Todos -----
def create_todo(session: Session, todo: TodoCreate) -> Todo:
    db_todo = Todo(title=todo.title)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo

def get_todos(session: Session) -> list[Todo]:
    return session.query(Todo).options(joinedload(Todo.items)).all()


def get_todo(session: Session, todo_id: int) -> Todo | None:
    return session.get(Todo, todo_id)

def toggle_todo_archived(session: Session, todo_id: int) -> Todo | None:
    db_todo = session.get(Todo, todo_id)
    if db_todo:
        db_todo.archived = not db_todo.archived
        session.commit()
        session.refresh(db_todo)
    return db_todo

def delete_todo(session: Session, todo_id: int):
    db_todo = session.get(Todo, todo_id)
    if db_todo:
        session.delete(db_todo)
        session.commit()
    return db_todo


# ----- Items -----
def add_item(session: Session, todo_id: int, item: TodoItemCreate) -> TodoItem | None:
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        return None
    db_item = TodoItem(item_title=item.item_title, todo_id=todo_id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def toggle_item_completed(session: Session, item_id: int) -> TodoItem | None:
    db_item = session.get(TodoItem, item_id)
    if db_item:
        db_item.completed = not db_item.completed
        session.commit()
        session.refresh(db_item)
    return db_item

def delete_item(session: Session, item_id: int):
    db_item = session.get(TodoItem, item_id)
    if db_item:
        session.delete(db_item)
        session.commit()
    return db_item
