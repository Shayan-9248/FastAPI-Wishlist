from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, crud, models
from users.authentication import get_current_active_user
from users.schemas import User
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/create", response_model=schemas.OrderItem, status_code=201)
async def create_order(
    cart: schemas.Cart,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await crud.create_order(cart, db, current_user)


@router.get("/", response_model=list[schemas.Order])
async def get_orders(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(database.get_db),
):
    return await crud.get_orders(current_user, db)
