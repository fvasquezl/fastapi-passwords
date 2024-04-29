from app.api.v1.models.post import DBPost
from app.core.database import TimeStampedModel
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class DBUser(TimeStampedModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    full_name: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relacion con Post
    posts: Mapped[List[DBPost]] = relationship(back_populates="owner")
