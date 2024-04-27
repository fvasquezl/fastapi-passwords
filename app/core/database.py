from datetime import datetime
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column


# SQLAlchemy
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create a declarative database
class Base(DeclarativeBase):
    pass


class NotFoundError(Exception):
    pass


class TimeStampedModel(Base):
    __abstract__ = True
    created_at = mapped_column(DateTime(timezone=True), default=datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=datetime.now())


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
