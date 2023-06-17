from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


class Item(BaseModel): #define video source's stucte
    name: str
    source: str
    number: int


app = FastAPI() #init app


@app.get("/videos/{video_id}") #start a api for get videos
async def read_item(video_id: int):
    return {"video_id": video_id}


@app.post("/videos", response_model=Item) #start a api for add video sources
async def create_item(item: Item):
    print(item)
    return item