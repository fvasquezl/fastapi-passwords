from sqlalchemy import Column, Integer, String
from config.database import Base


class TagDB(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    slug = Column(String(45))
