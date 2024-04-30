from datetime import datetime
from typing import Any, Dict, Optional
from fastapi import HTTPException
from pydantic import BaseModel
from app.api.v1.models.user import DBUser
from sqlalchemy.orm import Session
from app.core.validator import UniqueEmailStr

from app.auth.security import get_password_hash
from app.core.hashing import Hasher


#
class UserBase(BaseModel):
    username: str
    email: UniqueEmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str

    # Encriptar el Password
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(**kwargs)
        data.pop("password")
        data["hashed_password"] = Hasher.get_password_hash(self.password)
        return data


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

    db_user = DBUser(**user.model_dump(exclude=None))
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

    # Iterar sobre los datos de actualización y actualizar los valores
    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

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
