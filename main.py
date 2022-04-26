from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

items = {}

app = FastAPI()

@app.get("/")
def root ():
    global items
    return items

@app.post("/items/")
async def create_item(item: Item):
    global items
    items = item
    return item