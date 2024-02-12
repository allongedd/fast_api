from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Fake database
fake_items_db = [{"item_name": "foo"}, {"item_name": "bar"}, {"item_name": "baz"}]


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Endpoint to fetch all items
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# Endpoint to fetch a specific item by its index
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return fake_items_db[item_id]


# Endpoint to create a new item
@app.post("/items/")
def create_item(item: dict):
    fake_items_db.append(item)
    return {"message": "Item created successfully", "item": item}
