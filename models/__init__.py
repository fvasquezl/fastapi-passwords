from config.database import Base, engine

from . import category_model, post, user, tag_model

Base.metadata.create_all(bind=engine)
