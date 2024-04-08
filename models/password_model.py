from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class PasswordDB(Base):
    __tablename__ = "passwords"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    slug = Column(String(45))
    extract = Column(String(45))
    body = Column(String(45))
    status = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("CategoryDB", back_populates="passwords")
    user = relationship("UserDB", back_populates="passwords")
