from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# instantiation of router
router = APIRouter()


# model of user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


# fake db users
users_list = [User(id=1, name="Julian", surname="Lago", url="https://github.com/JuliusWhite", age=24),
              User(id=2, name="Brais", surname="Moure", url="https://mouredev.com", age=35)]

# petitions
@router.get("/users")
async def users():
    return users_list

# Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)


@router.post("/user", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="user alreay exists")

    users_list.append(user)
    return user


@router.put("/user", status_code=202)
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(
            status_code=400, detail="client error updating user")


@router.delete("/user/{id}", status_code=202)
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        raise HTTPException(status_code=404, detail="user not found")


# method to search for a spcific user
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "value not found"}
