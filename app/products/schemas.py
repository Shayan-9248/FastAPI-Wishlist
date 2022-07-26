from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    link: str = Field(...)

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    title: Optional[str] = None
    unit_price: Optional[str] = None
    discount: Optional[str] = None
    total_price: Optional[str] = None
    score: Optional[str] = None
    is_available: Optional[bool] = True
    is_purchased: Optional[bool] = False
    create_date: datetime
