from fastapi import APIRouter
from app.core.database import Base, engine
from app.api.v1.models import category, post, tag, user
from app.api.v1.endpoints import users, posts, categories, tags, tokens

api_router = APIRouter()
api_router.include_router(tokens.router, prefix="/token", tags=["Tokens"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(tags.router, prefix="/tags", tags=["Tags"])
api_router.include_router(posts.router, prefix="/posts", tags=["Posts"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])

# Crea la base de datos desde los modelos
Base.metadata.create_all(bind=engine)
