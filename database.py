import os
import asyncpg
import yaml

# 获取当前脚本的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接配置文件的绝对路径
config_path = os.path.join(script_dir, "config.yaml")

# 加载配置文件
config = yaml.safe_load(open(config_path))


async def create_pool():
    return await asyncpg.create_pool(
        host=config["database"]["host"],
        port=config["database"]["port"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["database"],
    )


async def get_connection():
    pool = await create_pool()
    async with pool.acquire() as conn:
        yield conn
