from fastapi import FastAPI,Query
from typing import Annotated
app = FastAPI()

@app.get("/")
def read_data():
    return {"status": "OK"}


@app.get("/items/{item_id}")
def read_item(item_id:int,
              q:Annotated[list[str]|None,Query(max_length=30)]=None,
              short: bool = False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if short:
        item.update(
            {"description": "This is a long description"}
        )
    return item