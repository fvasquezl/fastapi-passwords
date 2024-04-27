from typing import List
from sqlalchemy import Integer, String
from app.api.v1.models.post import DBPost
from app.core.database import TimeStampedModel
from sqlalchemy.orm import relationship, Mapped, mapped_column


class DBUser(TimeStampedModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    # Relacion con Post
    posts: Mapped[List[DBPost]] = relationship(back_populates="owner")
