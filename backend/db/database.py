from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# creation de l'engine
DATABASE_URL = 'sqlite:///db/todo.db'
engine = create_engine(DATABASE_URL)

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