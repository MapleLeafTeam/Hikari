import asyncio
import asyncpg
import yaml

config = yaml.safe_load(open("config.yaml"))

async def create_tables():
    conn = await asyncpg.connect(
        host=config["database"]["host"],
        port=config["database"]["port"],
        user=config["database"]["user"],
        password=config["database"]["password"],
        database=config["database"]["database"],
    )

    # 创建动漫数据表
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS anime (
            id SERIAL PRIMARY KEY,
            type VARCHAR(255),
            description TEXT,
            status VARCHAR(255),
            playback_link VARCHAR(255)
        )
        """
    )

    # 创建用户数据表
    await conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
        """
    )

    await conn.close()

asyncio.run(create_tables())
