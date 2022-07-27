from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import models, schemas, crud
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/carts", tags=["carts"])


@router.post("/create", status_code=201)
async def create_cart(db: Session = Depends(database.get_db)):
    return await crud.create_cart(db)


@router.post("/item/create", status_code=201)
async def create_cart_item(
    cart_item: schemas.CartItemCreate, db: Session = Depends(database.get_db)
):
    return await crud.create_cart_item(cart_item, db)


@router.get("/item/{cart_id}")
async def get_cart_item(cart_id: str, db: Session = Depends(database.get_db)):
    return await crud.get_cart_item(cart_id, db)
