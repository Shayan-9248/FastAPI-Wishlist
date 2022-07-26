from datetime import datetime

from sqlalchemy import Column, Text, Integer, ForeignKey, DateTime

import database


class Comment(database.Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    create_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.product_id} - {self.user_id})"
