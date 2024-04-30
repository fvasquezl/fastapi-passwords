from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.api.schemas.token import Token
from app.api.schemas.user import (
    User,
    UserCreate,
)
from app.api.v1.models.user import DBUser
from app.auth.jwt_handler import create_access_token, get_current_active_user
from app.core.database import get_db
from app.core.config import settings
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.jwt_handler import pwd_context

router = APIRouter()


@router.post("/users/")
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe
    existing_user = (
        db.query(DBUser).filter(DBUser.username == user_data.username).first()
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Crea el usuario y almacena la contraseña con hash
    hashed_password = pwd_context.hash(user_data.password)
    user = User(username=user_data.username, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)

    # Genera un token de acceso para el nuevo usuario
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    # Guarda el token en la base de datos
    db_token = Token(access_token=access_token, token_type="bearer", user_id=user.id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return {"user": user, "access_token": access_token, "token_type": "bearer"}


# @router.post("/users/", response_model=User)
# def create_user(
#     current_user: Annotated[User, Depends(get_current_active_user)],
#     user: UserCreate,
#     db: Session = Depends(get_db),
# ):
#     db_user = DBUser(**user.model_dump())
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
