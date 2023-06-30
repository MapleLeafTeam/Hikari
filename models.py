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


class Comment(BaseModel):
    id: int
    user_id: int
    anime_id: int
    comment: str


class CommentCreate(BaseModel):
    user_id: int
    comment: str


class Rating(BaseModel):
    id: int
    user_id: int
    anime_id: int
    rating: float


class RatingCreate(BaseModel):
    user_id: int
    rating: float


class Favorite(BaseModel):
    id: int
    user_id: int
    anime_id: int


class FavoriteCreate(BaseModel):
    anime_id: int


class PlayHistory(BaseModel):
    id: int
    user_id: int
    anime_id: int


class PlayHistoryCreate(BaseModel):
    anime_id: int
