from fastapi import FastAPI, Depends, HTTPException
from db import get_db, engine, create_table
import models, schemas, crud
from sqlalchemy.orm import Session

app = FastAPI()
create_table()

@app.post("/books", response_model = schemas.BookOut)
def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.get("/books", response_model = list[schemas.BookOut])
def get_all_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model = schemas.BookOut)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model = schemas.BookOut)
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}", response_model = schemas.BookOut)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book