from fastapi import FastAPI

from users.api.v1 import router as users_router


app = FastAPI()
app.include_router(users_router)
