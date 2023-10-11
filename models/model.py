from pydantic import BaseModel


class User(BaseModel):
    name: str
    username: str
    email: str
    password: str


class Movies(BaseModel):
    title: str
    slug: str
    descripton: str
    tags: list
    duration: int
