from __future__ import annotations
from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
import app.api.v1.models.post_tags

if TYPE_CHECKING:
    from app.api.v1.models.category import DBCategory
    from app.api.v1.models.user import DBUser
    from app.api.v1.models.tag import DBTag
else:
    DBUser = "DBUser"
    DBCategory = "DBCategory"
    DBTag = "DBTag"


class DBPost(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String)
    extract: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)
    status: Mapped[int]
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # Relaciones
    category: Mapped[DBCategory] = relationship(back_populates="posts")
    owner: Mapped[DBUser] = relationship(back_populates="posts")
    tags: Mapped[List[DBTag]] = relationship(
        secondary="post_tags", back_populates="posts"
    )
