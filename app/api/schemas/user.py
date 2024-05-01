from app.core.hashing import Hasher
from app.core.validator import UniqueEmailStr
from datetime import datetime
from pydantic import BaseModel
from typing import Any, Dict, Optional
from app.api.v1.models.user import DBUser
from sqlalchemy.orm import Session
from fastapi import HTTPException


class UserBase(BaseModel):
    username: str
    email: UniqueEmailStr


class UserCreate(UserBase):
    password: str

    # Encriptar el Password
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        data = super().model_dump(**kwargs)
        data.pop("password")
        data["hashed_password"] = Hasher.get_password_hash(self.password)
        return data


class User(UserBase):
    id: int
    is_disabled: bool | None = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class UserResponse(User):
    class Config:
        from_attributes = True


def create_db_user(user: UserCreate, db: Session):
    db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = DBUser(**user.model_dump(exclude=None))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
