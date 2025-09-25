import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "db")
os.makedirs(DB_DIR, exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(DB_DIR, 'todo.db')}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

class Base(DeclarativeBase):
    pass

# config session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_sessiondep():

    sessiondep = SessionLocal()
    try:
        yield sessiondep
    finally:
        sessiondep.close()