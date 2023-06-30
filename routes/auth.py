from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from app.models import User, UserCreate, UserLogin
from app.database import get_connection

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/apis/register")
async def register_user(user_data: UserCreate, conn=Depends(get_connection)):
    # 用户注册逻辑
    hashed_password = pwd_context.hash(user_data.password)
    query = "INSERT INTO users (username, password) VALUES ($1, $2)"
    await conn.execute(query, user_data.username, hashed_password)
    return {"message": "User registered successfully"}


@router.post("/apis/login")
async def login_user(user_data: UserLogin, conn=Depends(get_connection)):
    # 用户登录逻辑
    query = "SELECT username, password FROM users WHERE username = $1"
    result = await conn.fetchrow(query, user_data.username)
    if result is None:
        return {"message": "Invalid username or password"}

    username, hashed_password = result["username"], result["password"]
    if not pwd_context.verify(user_data.password, hashed_password):
        return {"message": "Invalid username or password"}

    return {"message": "Login successful", "username": username}
