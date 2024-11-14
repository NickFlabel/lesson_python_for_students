from fastapi import FastAPI

from models import Item

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
async def read_items(offset: int = 0, limit: int = 10):
    items = [{"item_id": i} for i in range(offset, offset + limit)]
    return {"items": items}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return {"item": item}
