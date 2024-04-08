from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class PasswordTagDB(Base):
    __tablename__ = "password_tag"

    password_id = Column(Integer, ForeignKey("passwords.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)

    password = relationship("PasswordDB", back_populates="tags")
    tag = relationship("TagDB", back_populates="passwords")
