from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from schemas import (
    Password,
    PasswordCreate,
)
from models.password_model import PasswordDB

password_router = APIRouter()


def get_db(request: Request):
    return request.state.db


# Rutas para contraseñas


@password_router.post("/passwords/", response_model=Password)
def create_password(password: PasswordCreate, db: Session = Depends(get_db)):
    db_password = PasswordDB(**password.dict())
    db.add(db_password)
    db.commit()
    db.refresh(db_password)
    return db_password


@password_router.get("/passwords/{password_id}", response_model=Password)
def read_password(password_id: int, db: Session = Depends(get_db)):
    db_password = db.query(PasswordDB).filter(PasswordDB.id == password_id).first()
    if db_password is None:
        raise HTTPException(status_code=404, detail="Password not found")
    return db_password
