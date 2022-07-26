from pydantic import BaseModel
from datetime import datetime


class CommentBase(BaseModel):
    content: str
    product_id: int

    class Config:
        orm_mode = True


class CommentCreate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    create_date: datetime
    update_date: datetime


class CommentUpdate(BaseModel):
    content: str
