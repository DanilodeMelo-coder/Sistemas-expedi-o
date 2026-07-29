from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

database_url = 'sqlite:///example.db'

engine = create_engine(database_url,
                       connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_session():

    db= sessionmaker()

    try:

        yield db

    finally:

        db.close()  