from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .category_model import CategoryDB
from .user_model import UserDB
from .tag_model import TagDB


association_table = Table(
    "association",
    Base.metadata,
    Column("password_id", Integer, ForeignKey("passwords.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class PasswordDB(Base):
    __tablename__ = "passwords"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(len(45))
    slug: Mapped[str] = mapped_column(len(45))
    extract: Mapped[str] = mapped_column(len(45))
    body: Mapped[str] = mapped_column(len(45))
    status: Mapped[int]
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    category: Mapped["CategoryDB"] = relationship(back_populates="passwords")

    user: Mapped["UserDB"] = relationship(back_populates="passwords")

    tags: Mapped[List[TagDB]] = relationship(
        secondary=association_table, back_populates="passwords"
    )
