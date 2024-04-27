from fastapi import APIRouter
from app.core.database import Base, engine
from app.api.v1.endpoints import users, posts  # , categories, tags
from app.api.v1.models import category, post, tag, user

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])
# api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
# api_router.include_router(tags.router, prefix="/tags", tags=["tags"])

# Crea la base de datos desde los modelos
Base.metadata.create_all(bind=engine)
