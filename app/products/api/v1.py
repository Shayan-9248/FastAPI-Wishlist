from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from users.authentication import get_current_active_user
from .. import models, schemas, crud
from users.models import User
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/create-link")
async def create_product_link(
    product: schemas.ProductCreate,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await crud.create_product_link(product, db, current_user)


@router.get("/all", response_model=list[schemas.Product])
async def get_all_products(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    return await crud.get_all_products(skip, limit, db)


@router.get("/unpurchased-list", response_model=list[schemas.Product])
async def get_unpurchased_products(
    db: Session = Depends(database.get_db)
):
    return await crud.get_unpurchased_products(db)
