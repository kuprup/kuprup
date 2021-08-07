#print('h')
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="Get a hello world json")
def hello(
    name: str = "Semen",
):
    """
    Hello world view
    1. processes `request`
    1. returns greeting
    """
    return {"Hello": name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}