from pydantic import BaseModel


class PostBase(BaseModel):
    name: str
    slug: str
    extract: str
    body: str
    status: int
    category_id: int
    user_id: int


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        from_attributes = True
