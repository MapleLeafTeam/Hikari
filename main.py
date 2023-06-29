from fastapi import FastAPI
from app.routes import auth, anime
from app.database import create_pool

app = FastAPI()

app.include_router(auth.router)
app.include_router(anime.router)


@app.on_event("startup")
async def startup():
    await create_pool()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)