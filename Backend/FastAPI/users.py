from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Julian", surname="Lago", url="https://github.com/JuliusWhite", age=24),
              User(id=2, name="Brais", surname="Moure", url="https://mouredev.com", age=35)]


@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "value not found"}
