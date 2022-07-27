from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import schemas, models


async def create_cart(db: Session):
    cart_db = models.Cart()
    db.add(cart_db)
    db.commit()
    db.refresh(cart_db)
    return cart_db


async def delete_cart(cart_id: str, db: Session):
    db_cart = db.query(models.Cart).filter(models.Cart.id == cart_id)

    if not db_cart.first():
        raise HTTPException(
            status_code=404, detail=f"Cart with id {cart_id} does not exists."
        )

    db_cart.delete()
    db.commit()
    return "Done"


async def create_cart_item(cart_item: schemas.CartItemCreate, db: Session):
    cart_item_db = models.CartItem(
        cart_id=cart_item.cart_id,
        product_id=cart_item.product_id,
    )
    db.add(cart_item_db)
    db.commit()
    db.refresh(cart_item_db)
    return cart_item_db


async def get_cart_item(cart_id: str, db: Session):
    return db.query(models.CartItem).filter(models.CartItem.cart_id == cart_id).all()
