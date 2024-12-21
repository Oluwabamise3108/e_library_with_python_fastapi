from fastapi import FastAPI
from app.routes import users, books, borrow_records

app = FastAPI()

# Include Routes
app.include_router(users.router, prefix="/api")
app.include_router(books.router, prefix="/api")
app.include_router(borrow_records.router, prefix="/api")
