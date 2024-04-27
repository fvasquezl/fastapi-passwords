from sqlalchemy import ForeignKey, Integer
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class PostTag(Base):
    __tablename__ = "post_tags"

    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("posts.id"), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tags.id"), primary_key=True
    )
