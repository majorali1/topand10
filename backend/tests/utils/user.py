from db.repository.user import create_a_new_user
from schemas.usercema import UserCreate
from sqlalchemy.orm import Session


def create_test_user(db: Session):
    user = UserCreate(username="popqwe", email="hey@myblog.waw", password="workout")
    user = create_a_new_user(db=db, user=user)
    return user
