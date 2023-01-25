from fastapi import FastAPI, HTTPException
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

# Query


@app.get("/userquery/")
async def user(id: int):
    return search_user(id)


@app.post("/user", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="user alreay exists")

    users_list.append(user)
    return user


@app.put("/user")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "user not updated"}


@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "user not found"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "value not found"}
