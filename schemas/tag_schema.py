from pydantic import BaseModel


class TagBase(BaseModel):
    name: str
    slug: str


class Tag(TagBase):
    id: int

    class Config:
        orm_mode = True


class PasswordTag(BaseModel):
    password_id: int
    tag_id: int
