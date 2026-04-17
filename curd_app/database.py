from sqlalchemy import create_engine  #Creates the connection between Python and the database.
from sqlalchemy.ext.declarative import declarative_base #Used to create a Base class for your models.
from sqlalchemy.orm import sessionmaker #Creates database sessions. Session = a conversation with the database.

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
'''
sqlite → database type

:/// → connection format

./test.db → file name in current directory
'''

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  
)

sessionLocal = sessionmaker(bind = engine, autocommit=False, autoflush=False)
Base = declarative_base()

