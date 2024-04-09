from typing import List
from sqlalchemy import Column, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column

from .password_model import PasswordDB, association_table


class TagDB(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(len(45))
    slug: Mapped[str] = mapped_column(len(45))

    passwords = Mapped[List[PasswordDB]] = relationship(
        secondary=association_table, back_populates="tags"
    )
