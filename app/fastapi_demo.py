from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI(title="Test API", version="0.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

# example: /items/1?v=test
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(ge=1, description="Item ID")], 
    v: Annotated[str | None, Query(max_length=10)]
):
    return {"item_id": item_id, "v": v}

class Item(BaseModel):
    name: str = ""
    tags: list[str] = []

temp_db: dict[int, Item] = {}

# example: {}"name": "user", "tags": ["human"]}
@app.post("/items/", status_code=201)
async def create_item(item: Item):
    item_id = len(temp_db) + 1
    temp_db[item_id] = item
    return {"item_id": item_id, **item.model_dump()}
