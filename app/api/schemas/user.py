from datetime import datetime
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from app.api.v1.models.user import DBUser
from sqlalchemy.orm import Session

from app.auth.security import get_password_hash


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


# def read_db_user(user_id: int, session: Session) -> DBUser:
#     db_user = session.query(DBUser).filter(DBUser.id == user_id).first()
#     if db_user is None:
#         raise FileNotFoundError(f"user with id {user_id} not found.")
#     return db_user


# def create_db_user(user: UserCreate, db: Session) -> DBUser:
#     # Verificar si el email ya existe
#     db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     # Hashear la contraseña
#     password = get_password_hash(user.password)

#     # Crear el nuevo usuario
#     new_user = DBUser(
#         name: user.name,
#         email: user.email,
#         password=hashed_password,
#         full_name: str | None = None


#         email=user.email,
#         first_name=user.first_name,
#         last_name=user.last_name,

#         is_active=True,
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)


# db_user = DBUser(**user.model_dump(exclude_none=True))
# db_user.hashed_password = Hasher.get_password_hash(user.hashed_password)
# session.add(db_user)
# session.commit()
# session.refresh(db_user)
# return db_user
