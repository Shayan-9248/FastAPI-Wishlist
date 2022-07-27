from datetime import datetime
import uuid

from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
    String,
)

import database


def generate_uuid():
    return str(uuid.uuid4())


class Cart(database.Base):
    __tablename__ = "carts"

    id = Column(String, primary_key=True, default=generate_uuid, index=True)
    create_date = Column(DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.id})"


class CartItem(database.Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(
        String, ForeignKey("carts.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE", onupdate="CASCADE")
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.cart_id} - {self.product_id})"
