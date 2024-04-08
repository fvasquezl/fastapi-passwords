from pydantic import BaseModel


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
