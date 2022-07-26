from sqlalchemy.orm import Session

from users.authentication import get_current_active_user
from . import schemas, models


async def create_product_link(
    product: schemas.ProductCreate, db: Session, current_user: get_current_active_user
):
    product_db = models.Product(link=product.link, user_id=current_user.id)
    db.add(product_db)
    db.commit()
    db.refresh(product_db)
    return product_db
