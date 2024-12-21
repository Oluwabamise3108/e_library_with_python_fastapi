# E-Library API System

## Description
The **E-Library API System** is a simple application built using FastAPI for managing an online library. The API allows users to perform the following operations:
- Manage user accounts (create, update, deactivate).
- Manage books in the library (add, update, mark as unavailable).
- Borrow and return books.
- View borrowing records.

This project uses in-memory storage for simplicity and is ideal for understanding the basics of building RESTful APIs with FastAPI.

---

## Features
1. **User Management**:
   - Create, update, delete, and retrieve users.
   - Deactivate users.

2. **Book Management**:
   - Add, update, delete, and retrieve books.
   - Mark books as unavailable.

3. **Borrow and Return Books**:
   - Borrow books if available and not already borrowed by the user.
   - Return borrowed books and update their status.

4. **Borrow Records**:
   - View borrowing records for a specific user.
   - View all borrowing records.

---

## Requirements
Ensure you have the following installed:
- Python 3.9 or later
- Pip (Python package manager)

---

## Installation
1. Clone this repository:
   
   git clone https://github.com/yourusername/e-library-api-system.git
   cd e-library-api-system

2. Create and activate a virtual environment:
   
   python -m venv venv
   source venv/bin/activate       
   venv\Scripts\activate

3. Install dependencies:

   pip install fastapi uvicorn

   ---

## Running the Application

1. Start the FastAPI server:

   uvicorn main:app --reload

2. Open your browser and navigate to:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

---

## API Endpoints

User Endpoints
Method	Endpoint	                Description
POST	/users/	                    Create a new user
GET	    /users/{user_id}	        Retrieve a user by ID
PUT	    /users/{user_id}	        Update a user's information
DELETE	/users/{user_id}	        Delete a user by ID
PATCH	/users/{user_id}/deactivate	Deactivate a user

Book Endpoints
Method	Endpoint	                        Description
POST	/books/	                            Add a new book
GET	    /books/{book_id}	                Retrieve a book by ID
PUT	    /books/{book_id}	                Update a book's details
DELETE	/books/{book_id}	                Delete a book by ID
PATCH	/books/{book_id}/mark_unavailable	Mark a book as unavailable

Borrow Operations
Method	Endpoint	        Description
POST	/borrow/	        Borrow a book
PATCH	/return/{borrow_id}	Return a borrowed book

Borrow Records
Method	Endpoint	            Description
GET	/borrow/records/	        Retrieve all borrowing records
GET	/borrow/records/{user_id}	Retrieve records for a user

---

## Example Usage

1. Create a user:
POST /users/
{
    "name": "John Doe",
    "email": "johndoe@example.com"
}

2. Add a book:
POST /books/
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}


3. Borrow a book:
POST /borrow/
{
    "user_id": 1,
    "book_id": 2
}

---

## Testing

You can test the API endpoints using:

Swagger UI (/docs)
Tools like Postman or curl.

---

Future Improvements
- Add a database for persistent storage.
- Implement user authentication and authorization.
- Include email notifications for overdue books.
