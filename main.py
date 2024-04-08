from fastapi import FastAPI

from routers.password_router import password_router
from routers.user_router import user_router
from middleware.db_session import DBSessionMiddleware

app = FastAPI()
app.add_middleware(DBSessionMiddleware)
app.include_router(user_router)
app.include_router(password_router)
