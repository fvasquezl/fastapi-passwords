from typing import List
from sqlalchemy import String
from app.core.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.api.v1.models.post import DBPost


class DBTag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String)

    # Relacion
    posts: Mapped[List[DBPost]] = relationship(
        secondary="post_tags", back_populates="tags"
    )
