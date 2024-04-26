from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# from .category_model import CategoryDB
from .user import User

# from .tag_model import TagDB


association_table = Table(
    "association",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    slug: Mapped[str] = mapped_column(String)
    extract: Mapped[str] = mapped_column(String)
    body: Mapped[str] = mapped_column(String)
    status: Mapped[int]
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # category: Mapped["CategoryDB"] = relationship(back_populates="passwords")

    user: Mapped[User] = relationship(back_populates="posts")

    # tags: Mapped[List[TagDB]] = relationship(
    #     secondary=association_table, back_populates="passwords"
    # )
