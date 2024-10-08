from db.repository.user import create_a_new_user
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from schemas.usercema import ShowUser
from schemas.usercema import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/users", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_a_new_user(user=user, db=db)
    return user
