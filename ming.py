from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import psycopg2
#创建
app = FastAPI()

conn = psycopg2.connect(
    host="your_host",
    database="your_database",
    user="your_username",
    password="your_password"
)

@app.post("/anime")
def add_anime(name: str, type: str, description: str, status: str, play_url: str):
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO anime (name, type, description, status, play_url) VALUES (%s, %s, %s, %s, %s)",
            (name, type, description, status, play_url)
        )
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to add anime")
    finally:
        cur.close()

    return {"message": "Anime added successfully"}

@app.get("/anime")
def get_anime():
    cur = conn.cursor()
    cur.execute("SELECT name, type, description, status, play_url FROM anime")
    anime_data = cur.fetchall()
    cur.close()

    anime_list = [
        {"name": name, "type": type, "description": description, "status": status, "play_url": play_url}
        for name, type, description, status, play_url in anime_data
    ]

    return JSONResponse(content=jsonable_encoder(anime_list))
