from typing import List

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class BlogUser(BaseModel):
    name: str
    email:str

    class Config():
        orm_mode = True


class ShowUser(BlogUser):
    blogs: List[Blog]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body:str
    creator: BlogUser

    class Config():
        orm_mode = True
