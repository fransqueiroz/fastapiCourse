from fastapi import APIRouter, Depends, Path
from pydantic import BaseModel, Field
from starlette import status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Todos

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool = Field(default=False)

@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoRequest, db: Session = Depends(get_db)):
    todo_model = Todos(**todo.dict())
    db.add(todo_model)
    db.commit()
    return

@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: Session = Depends(get_db)):
    return db.query(Todos).all()

@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: Session = Depends(get_db), todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Item not found")