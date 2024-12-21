from fastapi import APIRouter, HTTPException
from app.models import BorrowRecord, User, Book, borrow_records, users, books
from datetime import date

router = APIRouter()

# Borrow a Book
@router.post("/borrow", status_code=201)
def borrow_book(user_id: int, book_id: int):
    user = next((u for u in users if u.id == user_id and u.is_active), None)
    book = next((b for b in books if b.id == book_id and b.is_available), None)

    if not user:
        raise HTTPException(status_code=400, detail="User is not active or does not exist")
    if not book:
        raise HTTPException(status_code=400, detail="Book is not available")

    # Check if already borrowed
    if any(r.user_id == user_id and r.book_id == book_id and not r.return_date for r in borrow_records):
        raise HTTPException(status_code=400, detail="User has already borrowed this book")

    borrow_record = BorrowRecord(
        id=len(borrow_records) + 1,
        user_id=user_id,
        book_id=book_id,
        borrow_date=date.today()
    )
    borrow_records.append(borrow_record)
    book.is_available = False
    return {"message": "Book borrowed successfully", "record": borrow_record}

# Return a Book
@router.post("/return", status_code=200)
def return_book(record_id: int):
    record = next((r for r in borrow_records if r.id == record_id), None)
    if not record or record.return_date:
        raise HTTPException(status_code=400, detail="Invalid record or book already returned")

    book = next((b for b in books if b.id == record.book_id), None)
    if book:
        book.is_available = True

    record.return_date = date.today()
    return {"message": "Book returned successfully", "record": record}
