from fastapi import FastAPI

from users.api.v1 import router as users_router
from users.authentication import router as authentication_router
from products.api.v1 import router as products_router
from comments.api.v1 import router as comments_router


app = FastAPI()
app.include_router(users_router)
app.include_router(authentication_router)
app.include_router(products_router)
app.include_router(comments_router)
