from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./Book_store.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

sessionlocal = sessionmaker(autoflush=False, autocommit = False, bind = engine)

Base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind = engine)