from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, crud, models
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(tags=["users"], prefix="/users")


@router.post("/create", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail=f"User with id {user_id} does not exists"
        )
    return db_user
