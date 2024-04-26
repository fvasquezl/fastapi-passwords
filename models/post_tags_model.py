from sqlalchemy import Column, ForeignKey, Integer, Table
from .post import Post
from .tag_model import TagDB
from config.database import Base
from sqlalchemy.orm import relationship


post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey(Post.id)),
    Column("tag_id", Integer, ForeignKey(TagDB.id)),
)


# Relaciones
Post.tags = relationship(TagDB, secondary=post_tags, backref="posts")
TagDB.posts = relationship(Post, secondary=post_tags, backref="tags")
