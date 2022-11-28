
from fastapi import FastAPI, Request

from models import Item

def get_items():
    print("get_item")
    query = Item.query
    resultSet = query.all()
    results = list(map(lambda u:
                       {'id': u.id, 'name': u.description, 'description': u.description, 'price': u.price},
                       resultSet))
    return results


def get_items(id: int):
    print("get_item", id)
    query = Item.query
    resultSet = query.all()
    results = list(map(lambda u:
                       {'id': u.id, 'name': u.description, 'description': u.description, 'price': u.price},
                       resultSet))
    return results


app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_items(item_id)
    return item


@app.get("/items/")
async def read_item():
    return get_items()


@app.get("/")
async def root():
    return {"message": "Hello World"}


