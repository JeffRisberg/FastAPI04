from fastapi import FastAPI
from sqlalchemy import create_engine

from models.item import Item

app = FastAPI()

db_host = "localhost"
db_port = '3306'
db_name = 'fastapi04'
db_user = "developer"
db_password = "123456"

connect_str = "mysql+mysqlconnector://" + db_user + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_name
print(connect_str)
# app.config['SQLALCHEMY_DATABASE_URI'] = connect_str

engine = create_engine(connect_str)
conn = engine.connect()


def get_items():
    print("get_item")
    with engine.connect() as conn:
        stmt = "select * from items;"
        query = conn.execute(stmt)
        result_set = query.fetchall()
        results = list(map(lambda u:
                           {'id': u.id, 'name': u.name, 'description': u.description, 'price': u.price},
                           result_set))
        return results


def get_item(id: int):
    print("get_item", id)
    stmt = "select * from items where id=" + str(id)
    query = conn.execute(stmt)
    result_set = query.fetchall()
    results = list(map(lambda u:
                       {'id': u.id, 'name': u.name, 'description': u.description, 'price': u.price},
                       result_set))
    return results


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = get_item(item_id)
    return item


@app.get("/items/")
async def read_item():
    return get_items()


@app.get("/")
async def root():
    return {"message": "Hello World"}
