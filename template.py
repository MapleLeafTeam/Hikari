from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from database import get_connection
from models import Anime
import os

router = APIRouter()
t_dir = os.path.dirname(os.path.abspath(__file__))
t_path = os.path.join(t_dir, "templates")
templates = Jinja2Templates(directory=t_path)


@router.get("/")
async def get_anime_list(request: Request, conn=Depends(get_connection)):
    query = "SELECT * FROM anime"
    results = await conn.fetch(query)
    anime_list = [Anime(**result).dict() for result in results]
    return templates.TemplateResponse(
        "anime_list.html", {"request": request, "anime_list": anime_list}
    )


@router.get("/anime/{anime_id}")
async def get_anime(anime_id: int, request: Request, conn=Depends(get_connection)):
    query = "SELECT * FROM anime WHERE id = $1"
    result = await conn.fetchrow(query, anime_id)
    if result is None:
        return {"message": "Anime not found"}
    anime = Anime(**result)
    return templates.TemplateResponse(
        "anime_details.html", {"request": request, "anime": anime}
    )


@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
