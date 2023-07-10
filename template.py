from fastapi import Depends, APIRouter,request
from database import get_connection
from models import Anime
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_anime_list(conn=Depends(get_connection)):
    query = "SELECT * FROM anime"
    results = await conn.fetch(query)
    anime_list = [Anime(**result).dict() for result in results]
    return templates.TemplateResponse("anime_list.html", {"request": request, "anime_list": anime_list})

@router.get("/anime/{anime_id}")
async def get_anime(anime_id: int, conn=Depends(get_connection)):
    query = "SELECT * FROM anime WHERE id = $1"
    result = await conn.fetchrow(query, anime_id)
    if result is None:
        return {"message": "Anime not found"}
    anime = Anime(**result)
    return templates.TemplateResponse("anime_details.html", {"request": request, "anime": anime})
