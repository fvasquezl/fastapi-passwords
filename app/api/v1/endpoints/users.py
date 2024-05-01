from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas.token import create_db_token
from app.api.v1.models.token import DBToken
from app.api.schemas.user import (
    User,
    UserCreate,
    UserResponse,
    create_db_user,
)
from app.api.v1.models.user import DBUser
from app.auth.jwt_handler import create_access_token
from app.core.database import get_db
from app.core.config import settings
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# from app.auth.jwt_handler import pwd_context

router = APIRouter()


@router.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe

    db_user = create_db_user(user, db)
    # user_response = UserResponse.model_validate(db_user)

    # # Genera un token de acceso para el nuevo usuario
    # access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = create_access_token(
    #     data={"sub": db_user.username}, expires_delta=access_token_expires
    # )
    # expires_at = datetime.now(timezone.utc) + access_token_expires

    # # db_token = create_db_token(access_token, "bearer", db_user.id, expires_at)
    # create_db_token(db_user.id, access_token, expires_at, db)

    # # Guarda el token en la base de datos
    # db_token = DBToken(
    #     access_token=access_token,
    #     token_type="bearer",
    #     user_id=db_user.id,
    #     expires_at=expires_at,
    # )
    # db.add(db_token)
    # db.commit()
    # db.refresh(db_token)

    return User(**db_user.__dict__)


# {
#         "user": user_response,
#         "access_token": access_token,
#         "token_type": "bearer",
#     }


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
