from fastapi import APIRouter, Depends
from models import Anime, Comment, CommentCreate, Rating, RatingCreate
from database import get_connection

router = APIRouter()


@router.get("/apis/anime/{anime_id}")
async def get_anime(anime_id: int, conn=Depends(get_connection)):
    # 获取动漫信息的逻辑
    query = "SELECT * FROM anime WHERE id = $1"
    result = await conn.fetchrow(query, anime_id)
    if result is None:
        return {"message": "Anime not found"}

    anime = Anime(**result)
    return anime.dict()


@router.get("/apis/anime")
async def get_anime_list(conn=Depends(get_connection)):
    # 获取动漫列表的逻辑
    query = "SELECT * FROM anime"
    results = await conn.fetch(query)
    anime_list = [Anime(**result).dict() for result in results]
    return anime_list

@router.post("/apis/anime/{anime_id}/comments")
async def create_comment(anime_id: int, comment_data: CommentCreate, conn=Depends(get_connection)):
    # 创建评论的逻辑
    query = "INSERT INTO comments (user_id, anime_id, comment) VALUES ($1, $2, $3)"
    await conn.execute(query, comment_data.user_id, anime_id, comment_data.comment)
    return {"message": "Comment created successfully"}


@router.get("/apis/anime/{anime_id}/comments")
async def get_comments(anime_id: int, conn=Depends(get_connection)):
    # 获取动漫评论的逻辑
    query = "SELECT * FROM comments WHERE anime_id = $1"
    results = await conn.fetch(query, anime_id)
    comments = [Comment(**result).dict() for result in results]
    return comments


@router.post("/apis/anime/{anime_id}/ratings")
async def create_rating(anime_id: int, rating_data: RatingCreate, conn=Depends(get_connection)):
    # 创建评分的逻辑
    query = "INSERT INTO ratings (user_id, anime_id, rating) VALUES ($1, $2, $3)"
    await conn.execute(query, rating_data.user_id, anime_id, rating_data.rating)
    return {"message": "Rating created successfully"}


@router.get("/apis/anime/{anime_id}/ratings")
async def get_ratings(anime_id: int, conn=Depends(get_connection)):
    # 获取动漫评分的逻辑
    query = "SELECT * FROM ratings WHERE anime_id = $1"
    results = await conn.fetch(query, anime_id)
    ratings = [Rating(**result).dict() for result in results]
    return ratings