from pydantic import EmailStr
from sqlalchemy.orm import Session

from . import models, schemas
from .hashing import Hash


async def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


async def get_user_by_email(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()


async def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
