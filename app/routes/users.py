from fastapi import APIRouter, HTTPException
from app.models import User, users

router = APIRouter()

# Create a User
@router.post("/users", status_code=201)
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully", "user": user}

# Get All Users
@router.get("/users")
def get_users():
    return users

# Get User by ID
@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Deactivate User
@router.patch("/users/{user_id}/deactivate")
def deactivate_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = False
    return {"message": "User deactivated successfully", "user": user}
