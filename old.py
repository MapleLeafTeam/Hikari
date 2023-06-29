from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import psycopg2

class Item(BaseModel): #define video source's stucte
    name: str
    source: str
    number: int


app = FastAPI() #init app


@app.get("/apis/get_video/{video_id}") #start a api for get videos
async def read_item(video_id: int):
    for i in range(len(datebase)):
            if i == video_id:
                 video_source = i

    return {"source": i}


@app.post("/apis/add_source", response_model=Item) #start a api for add video sources
async def create_item(item: Item):
    return item