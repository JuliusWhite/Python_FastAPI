# For any command in windows add 'py -m' before the command

# For installing FastAPI -> 'pip install "fastapi[all]"'

# For starting server in localhost (http://127.0.0.1:8000) -> uvicorn main:app --reload, attending to 'app' and 'main'
# 'Ctrl + C' tp stop it

# Documentation -> http://127.0.0.1:8000/docs for Swagger 
#               or http://127.0.0.1:8000/redoc for Redocly

from fastapi import FastAPI
from routers import products, users

app = FastAPI()

# routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hello World"

@app.get("/url")
async def url():
    return { "url_github": "https://github.com/JuliusWhite"}