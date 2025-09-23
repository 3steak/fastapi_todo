from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# creation de l'engine
DATABASE_URL = 'sqlite:///db/todo.db'
engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

# config session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Créer une session pour les opérations sur la base."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()