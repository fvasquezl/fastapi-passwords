from datetime import datetime
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from app.api.v1.models.user import DBUser
from sqlalchemy.orm import Session

from app.auth.security import get_password_hash
from app.core.hashing import Hasher


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = True


class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        from_attributes = True


# Get All Users
def get_all_users(db: Session):
    try:
        db_users = db.query(DBUser).all()
        return db_users
    except Exception as e:
        db.rollback()
        raise e


# Create User
def create_db_user(user: UserCreate, db: Session):
    db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = DBUser(**user.model_dump(exclude="password"))
    db_user.hashed_password = Hasher.get_password_hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_db_user(user_id: int, db: Session):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def update_db_user(user_id: int, user: UserUpdate, db: Session):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.model_dump(exclude_none=True).items():
        setattr(db_user, key, value)

    # Si se proporciona una nueva contraseña, hashearla y actualizarla
    if user.password:
        db_user.hashed_password = Hasher.get_password_hash(user.password)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_db_user(user_id: int, db: Session):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return db_user
