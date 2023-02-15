# For any command in windows add 'py -m' before the command

# For installing FastAPI -> 'pip install "fastapi[all]"'

# For starting server in localhost (http://127.0.0.1:8000) -> uvicorn main:app --reload, attending to 'app' and 'main'
# 'Ctrl + C' tp stop it

# Documentation -> http://127.0.0.1:8000/docs for Swagger
#               or http://127.0.0.1:8000/redoc for Redocly


# imports
from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

# instantiation of FastAPI
app = FastAPI()

# routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# petitions


@app.get("/")
async def index():
    return FileResponse('index.html')


@app.get("/url")
async def url():
    return {"url_github": "https://github.com/JuliusWhite"}
