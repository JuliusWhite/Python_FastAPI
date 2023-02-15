from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# user model
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# userDB model
class UserDB(User):
    password: str

# fake db users
users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": True,
        "password": "123456"
    },
    "julian_lago": {
        "username": "julian_lago",
        "full_name": "Julián Lago",
        "email": "julianlago@gmail.com.com",
        "disabled": False,
        "password": "654321"
    }
}

# dependency criterion
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="incorrect credentials", 
        headers={"WWW-Autenticate": "Bearer"})

    if user.disabled:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="inactive user")

    return user

    


@app.post("/login")
async def login (form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="incorrect user")
    
    user = search_user(form.username)
    if form.password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="incorrect password")

    return {"access_token" : user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user


# mehtod for searching a user
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])


