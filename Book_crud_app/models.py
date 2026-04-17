from db import Base
from sqlalchemy import Column,Integer,String

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    description = Column(String(500))
    year = Column(Integer)


    """
    Added:

    nullable=False for required fields

    Length limits

    Cleaner naming
    """