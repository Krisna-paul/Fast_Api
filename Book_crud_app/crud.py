from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate, BookUpdate

def create_book(db: Session, data: BookCreate):
    new_book = Book(**data.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, book_id: int, data: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    for key, value in data.model_dump().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
    return book