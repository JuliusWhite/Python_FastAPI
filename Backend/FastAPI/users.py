from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Julian", surname="Lago", url="https://github.com/JuliusWhite", age=24),
            User(name="Brais", surname="Moure", url="https://mouredev.com", age=35)]

@app.get("/users")
async def users():
    return users_list