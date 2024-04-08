from config.database import Base, engine

from . import category_model, user_model, password_model, tag_model, password_tag_model

Base.metadata.create_all(bind=engine)
