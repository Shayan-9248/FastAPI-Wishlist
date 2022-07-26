from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import relationship

import database


class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    create_date = Column(DateTime, default=datetime.now)

    products = relationship("Product", back_populates="user")

    def __repr__(self) -> str:
        return f"{self.__class__.__tablename__} ({self.email} - {self.id})"
