from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/hello/{name}")
async def hello(request: Request, name: str):
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})