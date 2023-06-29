import asyncpg
import yaml

config = yaml.safe_load(open("config.yaml"))


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
