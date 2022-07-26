from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    link: str = Field(...)
