from pydantic import EmailStr
from fastapi import Depends
from app.api.v1.models.user import DBUser
from sqlalchemy.orm import Session
from app.core.database import get_db


class UniqueEmailStr(EmailStr):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, values, config, field):
        # validación de formato de email
        v = EmailStr.validate(v, values, config, field)

        # Verificación de usuario actual
        if "id" in values and v == values["email"]:
            return v  # Permitir el mismo email si es del usuario actual

        # Verificación de email único
        db: Session = Depends(get_db)
        existing_user = db.query(DBUser).filter(DBUser.email == v).first()
        if existing_user:
            raise ValueError("Email already registered")
        return v
