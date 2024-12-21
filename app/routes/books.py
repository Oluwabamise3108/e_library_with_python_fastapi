from fastapi import APIRouter, HTTPException
from app.models import Book, books

router = APIRouter()

# Create a Book
@router.post("/books", status_code=201)
def create_book(book: Book):
    books.append(book)
    return {"message": "Book created successfully", "book": book}

# Get All Books
@router.get("/books")
def get_books():
    return books

# Mark Book as Unavailable
@router.patch("/books/{book_id}/unavailable")
def mark_book_unavailable(book_id: int):
    book = next((b for b in books if b.id == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book.is_available = False
    return {"message": "Book marked as unavailable", "book": book}
