from core.hashing import Hasher
from db.models.users import User
from schemas.usercema import UserCreate
from sqlalchemy.orm import Session


def create_a_new_user(user: UserCreate, db: Session):
    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
