
#print('h')
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping", summary="Returns a message pong")
def hello():
    return {"message": "pong"}

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str] = None):
#    return {"item_id": item_id, "q": q}