from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    slug: str


class TagCreate(TagBase):
    pass


class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True


class PostTag(BaseModel):
    post_id: int
    tag_id: int
