from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

# User Model
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

# Book Model
class Book(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True

# Borrow Record Model
class BorrowRecord(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None

# In-Memory Storage
users: List[User] = []
books: List[Book] = []
borrow_records: List[BorrowRecord] = []
