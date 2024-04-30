from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.schemas.token import Token
from app.api.v1.models.user import DBUser
from app.auth.jwt_handler import create_access_token
from app.core.config import settings
from app.core.database import get_db
from app.core.hashing import Hasher

router = APIRouter()


@router.post("/", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(DBUser).filter(DBUser.email == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not Hasher.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    # Guarda el token en la base de datos
    db_token = Token(access_token=access_token, token_type="bearer", user_id=user.id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)

    return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/refresh")
# def refresh_token(refresh_token: str = Depends(oauth2_scheme)):
#     # ... lógica para validar el token de refresco y generar un nuevo token de acceso ...


# @router.post("/revoke")
# def revoke_token(token: str = Depends(oauth2_scheme)):
#     # ... lógica para invalidar el token ...


# @router.post("/refresh")
# def refresh_token(refresh_token: str = Depends(refresh_token_scheme)):
#     # ... lógica para validar el token de refresco y generar un nuevo token de acceso ...
#     # ... devuelve el nuevo token de acceso ...
