from sqlalchemy import Column, DateTime, Integer, String
from config.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    email = Column(String(45))
    password = Column(String(45))
    create_at = Column(DateTime)

    posts = relationship("Post", back_populates="user")
