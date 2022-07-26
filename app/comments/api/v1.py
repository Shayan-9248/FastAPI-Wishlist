from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from users.schemas import User
from users.authentication import get_current_active_user
import database

models.database.Base.metadata.create_all(bind=database.engine)

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("/create")
async def create(
    request: schemas.CommentBase,
    db: Session = Depends(database.get_db),
    current_user: User = Depends(get_current_active_user),
):
    return await crud.create_comment(db, request, current_user)


@router.get("/{product_id}")
async def read_product_comments(
    product_id: int, db: Session = Depends(database.get_db)
):
    return await crud.get_product_comments(db, product_id)


@router.put("/update/{comment_id}")
async def update_comment(
    comment_id: int,
    comment: schemas.CommentUpdate,
    db: Session = Depends(database.get_db),
):
    return await crud.update_comment(db=db, comment_id=comment_id, comment=comment)


@router.delete("/delete/{comment_id}")
async def delete_comment(comment_id: int, db: Session = Depends(database.get_db)):
    return await crud.delete_comment(db=db, comment_id=comment_id)
