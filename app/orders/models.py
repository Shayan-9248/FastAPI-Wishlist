import enum

from sqlalchemy import Integer, ForeignKey, Boolean, Column, String, Enum
from sqlalchemy.orm import relationship

import database


class Status(enum.Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    FAILED = "failed"


class Order(database.Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String(20), Enum(Status), default=Status.PENDING)
    is_paid = Column(Boolean, default=False)

    order_items = relationship("OrderItem", back_populates="order")

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.id} - {self.user_id})"


class OrderItem(database.Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    order = relationship("Order", back_populates="order_items")

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.order_id} - {self.product_id})"
