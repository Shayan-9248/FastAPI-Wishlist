from fastapi import Depends
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
