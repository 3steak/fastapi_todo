from db.database import Base, engine, SessionLocal
from models.todo import Todo, TodoItem

# Création des tables
def create_tables():
    print("Création des tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables créées avec succès !")

# Ajout des todolists
def add_todos(todolist_name :str):
    session = SessionLocal()
    
    todolist = Todo(title=todolist_name)

    session.add(todolist)
    session.commit()
    session.refresh(todolist)
    return todolist
    
# add item in todo
def add_item(todo_id: int, item_title: str):
    session = SessionLocal()
    try:
        todoitem = TodoItem(item_title=item_title, todo_id=todo_id)
        session.add(todoitem)
        session.commit()
        session.refresh(todoitem)
        return todoitem    
    finally:
        session.close()


# Lire todo
def get_todos():
    session = SessionLocal()
    
    todos = session.query(Todo).all()
    return todos
        # for todo in todos:
        #     print(f"ID: {todo.id}, Title: {todo.title}, Archived: {todo.archived}")
        #     if todo.items:
        #         for item in todo.items:
        #             print(f"   - {item.item_title} (done={item.completed})")
        #     else:
        #         print("   (aucun item)")    
   

# Mettre a jour todo
# Supprimer todo
# Menu principal


def main_menu():
    print("Bonjour que voulez vous faire ?")
    print("1. Creer une TodoList.")
    print("2. Ajouter quelque chose a une todolist.")
    print("3. Afficher la ou les todolists.")
    print("0. Quitter")

    while True:
        choice = input("Faites un choix (0-4): ")

        if choice == "1":
            todolist_name = input("Entrez un nom de todolist: ")
            add_todos(todolist_name)
        elif choice == "2":
            add_item()
        elif choice == "3":
            get_todos()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Mauvais choix, recommencez svp")


if __name__ == "__main__":
    create_tables()
    main_menu()



    # todolist + item 
    # select todolist + ajout ou completed item + archived la todo

    
    # ajouter todo 
    #  afficher todo coté front