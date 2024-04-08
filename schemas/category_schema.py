from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    slug: str


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
