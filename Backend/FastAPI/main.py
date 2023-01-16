# For installing FastAPI -> " pip install "fastapi[all]" " or " py -m pip install "fastapi[all] " for windows

# For starting server in localhost (http://127.0.0.1:8000) -> " uvicorn main:app --reload ", attending to 'app' and 'main'

# Documentation -> http://127.0.0.1:8000/docs for Swagger or http://127.0.0.1:8000/redoc ofr Redocly

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World"

@app.get("/url")
async def url():
    return { "url_github": "https://github.com/JuliusWhite"}