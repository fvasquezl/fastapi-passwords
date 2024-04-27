from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.api.schemas.post import Post, PostCreate
from app.api.v1.models.post import DBPost
from app.core.database import get_db

router = APIRouter()


# Rutas para contraseñas


@router.post("/posts/", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = DBPost(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(DBPost).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
