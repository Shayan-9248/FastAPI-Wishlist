from sqlalchemy.orm import Session

from . import schemas, models
from carts.models import CartItem
from users.authentication import get_current_active_user


async def create_order(
    cart: schemas.Cart, db: Session, current_user: get_current_active_user
):
    db_order = models.Order(user_id=current_user.id, status="pending")
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    cart_item = db.query(CartItem).filter(CartItem.cart_id == cart.id).all()
    for c in cart_item:
        db_order_item = models.OrderItem(product_id=c.product_id, order_id=db_order.id)
        db.add(db_order_item)
        db.commit()
        db.refresh(db_order_item)
    return db_order_item
