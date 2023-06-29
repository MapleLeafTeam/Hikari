from typing import Union
from fastapi import FastAPI, HTTPException, Query, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import asyncpg
import asyncio
import yaml

app = FastAPI()

conn_pool = None


def load_config():
    # 从配置文件中加载数据库连接信息
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config


config = load_config()


@app.on_event("startup")
async def startup():
    global conn_pool
    # 创建数据库连接池
    conn_pool = await asyncpg.create_pool(
        host=config["database"]["host"],
        database=config["database"]["database"],
        user=config["database"]["user"],
        password=config["database"]["password"]
    )


@app.on_event("shutdown")
async def shutdown():
    # 关闭数据库连接池
    await conn_pool.close()


@app.post("/register")
async def register(username: str, password: str):
    async with conn_pool.acquire() as conn:
        try:
            async with conn.transaction():
                # 检查用户名是否已存在
                result = await conn.fetchrow("SELECT * FROM users WHERE username = $1", username)
                if result:
                    raise HTTPException(status_code=400, detail="Username already exists")

                # 插入新用户记录
                await conn.execute("INSERT INTO users (username, password) VALUES ($1, $2)", username, password)
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to register user")

    return {"message": "User registered successfully"}


@app.post("/login")
async def login(username: str, password: str):
    async with conn_pool.acquire() as conn:
        # 查询用户记录
        result = await conn.fetchrow("SELECT * FROM users WHERE username = $1 AND password = $2", username, password)

        if result:
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid username or password")


@app.post("/anime")
async def add_anime(id: int, name: str, type: str, description: str, status: str, play_url: str, token: str = Header(None)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    async with conn_pool.acquire() as conn:
        try:
            async with conn.transaction():
                # 插入动漫记录
                await conn.execute(
                    "INSERT INTO anime (id, name, type, description, status, play_url) VALUES ($1, $2, $3, $4, $5, $6)",
                    id, name, type, description, status, play_url
                )
        except Exception as e:
            raise HTTPException(status_code=500, detail="Failed to add anime")

    return {"message": "Anime added successfully"}


@app.get("/anime")
async def get_anime(category: str = Query(None, description="Filter anime by category"), token: str = Header(None)):
    if not verify_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    async with conn_pool.acquire() as conn:
        if category:
            # 根据类别筛选动漫记录
            anime_data = await conn.fetch(
                "SELECT id, name, type, description, status, play_url FROM anime WHERE type = $1",
                category
            )
        else:
            # 获取所有动漫记录
            anime_data = await conn.fetch("SELECT id, name, type, description, status, play_url FROM anime")

    anime_list = [
        {"id": record["id"], "name": record["name"], "type": record["type"],
         "description": record["description"], "status": record["status"], "play_url": record["play_url"]}
        for record in anime_data
    ]

    return JSONResponse(content=jsonable_encoder(anime_list))


def verify_token(token: str) -> bool:
    # 这里可以添加验证 token 的逻辑，例如从数据库或其他存储中验证
    return token == "mytoken"
