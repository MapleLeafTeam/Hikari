import psycopg2
import yaml

def load_config():
    # 从配置文件中加载数据库连接信息
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

config = load_config()

# 获取数据库连接信息
db_host = config["database"]["host"]
db_name = config["database"]["database"]
db_user = config["database"]["user"]
db_password = config["database"]["password"]

# 创建数据库连接
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
)

# 创建游标对象
cur = conn.cursor()

# 创建动漫数据表
cur.execute("""
    CREATE TABLE IF NOT EXISTS anime (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        description TEXT,
        status TEXT,
        play_url TEXT
    );
""")

# 创建用户数据表
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );
""")

# 提交事务
conn.commit()

# 关闭游标和连接
cur.close()
conn.close()

print("Anime table created successfully.")
