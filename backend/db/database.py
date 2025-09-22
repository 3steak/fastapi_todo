from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# creation de l'engine
DATABASE_URL = 'sqlite:///db/todo.db'
engine = create_engine(DATABASE_URL, echo=True)

# config session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    """Créer une session pour les opérations sur la base."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()