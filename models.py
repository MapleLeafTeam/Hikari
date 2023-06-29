from pydantic import BaseModel


class Anime(BaseModel):
    id: int
    type: str
    description: str
    status: str
    playback_link: str


class User(BaseModel):
    username: str


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
