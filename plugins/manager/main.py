from fastapi import APIRouter, Depends
from models import Anime
from database import get_connection

router = APIRouter()


@router.post("/plugins/anime")
async def create_anime(anime_data: Anime, conn=Depends(get_connection)):
    # 新增动漫的逻辑
    query = """
    INSERT INTO anime (type, description, status, playback_link)
    VALUES ($1, $2, $3, $4)
    RETURNING id
    """
    values = (anime_data.type, anime_data.description, anime_data.status, anime_data.playback_link)
    async with conn.transaction():
        result = await conn.fetchrow(query, *values)
        anime_id = result["id"]
    return {"message": "Anime created successfully", "anime_id": anime_id}
