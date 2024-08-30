from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models import User
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import SessionLocal

router = APIRouter()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

@router.post("/auth")
async def create_user(create_user_request: CreateUserRequest):
    create_user_model = User(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    return create_user_model



    return {"user": "authenticated"}