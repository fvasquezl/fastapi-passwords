from fastapi import FastAPI

# from app.api.v1.endpoints.posts import post_router
# from app.api.v1.endpoints.users import user_router
from app.api.v1.api import api_router

# from middleware.db_session import DBSessionMiddleware

app = FastAPI()
# app.add_middleware(DBSessionMiddleware)
app.include_router(api_router)


# app.include_router(user_router)
# app.include_router(post_router)
