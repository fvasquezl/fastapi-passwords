from pydantic import BaseModel
from typing import List, Optional


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    create_at: str

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    slug: str


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class PasswordBase(BaseModel):
    name: str
    slug: str
    extract: str
    body: str
    status: int
    category_id: int
    user_id: int


class PasswordCreate(PasswordBase):
    pass


class Password(PasswordBase):
    id: int

    class Config:
        orm_mode = True


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
