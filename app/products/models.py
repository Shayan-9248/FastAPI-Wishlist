from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean,
    DateTime,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

import database


class Product(database.Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    link = Column(String, nullable=False)
    title = Column(String, nullable=True)
    description = Column(Text)
    unit_price = Column(String)
    discount = Column(Integer)
    total_price = Column(String)
    score = Column(Integer)
    is_avaialable = Column(Boolean)
    is_purchased = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="products")

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.user_id} - {self.link})"
