from pydantic import BaseModel


class Cart(BaseModel):
    id: str


class Order(BaseModel):
    id: int
    user_id: int
    status: str = "pending"
    order_items: list = []

    class Config:
        orm_mode = True


class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int

    class Config:
        orm_mode = True
