from fastapi import APIRouter, Depends
from request.requests import CreateUserRequest
from infastructure.database import  SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from models.user import Users
from passlib.context import CryptContext

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/users')
async def list_of_users(db: Session = Depends(get_db)):
   users = db.query(Users).all()
   return users

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(db: db_dependency,
                   create_user_request: CreateUserRequest):
    user = Users(
        email= create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    db.add(user)
    db.commit()