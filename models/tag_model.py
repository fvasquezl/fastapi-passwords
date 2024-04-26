from typing import List
from sqlalchemy import Column, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column

from .post import Post, association_table


class TagDB(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String)

    posts: Mapped[List[Post]] = relationship(
        secondary=association_table, back_populates="tags"
    )
