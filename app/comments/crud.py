from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from users.authentication import get_current_active_user
from users.schemas import User


async def create_comment(
    db: Session,
    request: schemas.CommentBase,
    current_user: User = Depends(get_current_active_user),
):
    new_comment = models.Comment(
        user_id=current_user.id,
        product_id=request.product_id,
        content=request.content,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


async def get_product_comments(db: Session, product_id: int):
    return db.query(models.Comment).filter(models.Comment.id == product_id).all()


async def update_comment(comment_id: int, db: Session, comment: schemas.CommentUpdate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id)
    if not db_comment.first():
        raise HTTPException(
            status_code=404, detail=f"Comment with id {comment_id} does not exists."
        )
    db_comment.update(
        {
            models.Comment.content: comment.content,
        }
    )
    db.commit()
    return "Done"


async def delete_comment(comment_id: int, db: Session):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id)

    if not db_comment.first():
        raise HTTPException(
            status_code=404, detail=f"Comment with id {comment_id} does not exists."
        )

    db_comment.delete()
    db.commit()
    return "Done"
