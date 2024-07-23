# FastAPI04

Shows examples of using FastAPI and a database.

It shows how to use SQLAlchemy.

This is based on Chapter 5 of the book by "Sherwin John C. Tragura"

## Setup database

Name is "fastapi04"

```
create database fastapi04;
```

One table for items.

Add some records like:

```
insert into items (name, description,price, created_at, updated_at)
values ("Zealot", "Protoss action figure", 66, current_timestamp(), current_timestamp());
```

## Running this

To run it:

```
cd src
uvicorn main:app --reload
```

Then send HTTP requests to localhost:8000, such as:

http://localhost:8000/

http://localhost:8000/items

http://localhost:8000/items/2
