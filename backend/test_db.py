from db.database import Base, engine, SessionLocal
from models.todo import Todo, TodoItem

# Création des tables
def create_tables():
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès !")

# Ajout des todolists
def add_todos():
    session = SessionLocal()
    try:
        todolist1 = Todo(title="Courses")
        todolist2 = Todo(title="Sports")
        session.add_all([todolist1, todolist2])
        session.commit()
        print("Todolist ajoutées avec succès !")
    finally:
        session.close()

# add item in todo
def add_item():
    session = SessionLocal()
    try:
        todoitem1 = TodoItem(item_title = "pain", todo_id = 1)
        session.add(todoitem1)
        session.commit()
        print("TodoItem ajoutées avec succès !")
    finally:
        session.close()


# Lire todo
def get_todos():
    session = SessionLocal()
    try:
        todos = session.query(Todo).all()
        for todo in todos:
            print(f"ID: {todo.id}, Title: {todo.title}, Archived: {todo.archived}")
            if todo.items:
                for item in todo.items:
                    print(f"   - {item.item_title} (done={item.completed})")
            else:
                print("   (aucun item)")    
    finally:
        session.close()

# Mettre a jour todo
# Supprimer todo
# Menu principal
if __name__ == "__main__":
    create_tables()
    add_item()
    get_todos()