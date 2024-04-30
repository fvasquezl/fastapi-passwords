from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.schemas.user import (
    UserCreate,
    UserUpdate,
    User,
    create_db_user,
    delete_db_user,
    get_all_users,
    get_db_user,
    update_db_user,
)
from app.auth.oauth2 import get_current_user
from app.core.database import get_db
from app.auth.oauth2 import get_current_user

router = APIRouter()


@router.get("/", response_model=List[User])
def get_user(db: Session = Depends(get_db)):
    db_users = get_all_users(db)
    return User(**db_users.__dict__)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(
    current_user: Annotated[User, Depends(get_current_user)],
    user: UserCreate,
    db: Session = Depends(get_db),
):
    db_user = create_db_user(user, db, current_user)
    return User(**db_user.__dict__)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_db_user(user_id, db)
    return User(**db_user.__dict__)


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = update_db_user(user_id, user, db, get_current_user)
    return User(**db_user.__dict__)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_db_user(user_id, db)
    return User(**db_user.__dict__)


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user
