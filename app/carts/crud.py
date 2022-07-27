from fastapi import APIRouter
from sqlalchemy.orm import Session

from . import schemas, models


async def create_cart(db: Session):
    cart_db = models.Cart()
    db.add(cart_db)
    db.commit()
    db.refresh(cart_db)
    return cart_db


async def create_cart_item(cart_item: schemas.CartItemCreate, db: Session):
    cart_item_db = models.CartItem(
        cart_id=cart_item.cart_id,
        product_id=cart_item.product_id,
    )
    db.add(cart_item_db)
    db.commit()
    db.refresh(cart_item_db)
    return cart_item_db
