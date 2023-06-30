from fastapi import APIRouter, Depends
from models import Anime
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