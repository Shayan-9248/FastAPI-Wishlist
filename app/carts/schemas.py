from pydantic import BaseModel


class CartItemBase(BaseModel):
    cart_id: str
    product_id: int

    class Config:
        orm_mode = True


class CartItemCreate(CartItemBase):
    pass


class CartItem(CartItemBase):
    id: int
