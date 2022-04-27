from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    payer: str
    points: int
    date: datetime

items = {}

app = FastAPI()

@app.get("/")
def root ():
    global items
    print(items.date.strftime('%Y-%m-%dT%H:%M:%SZ'))
    return items

@app.post("/items/")
async def create_item(item: Item):
    global items
    items = item
    return item