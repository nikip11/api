from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import jwt, JWTError
from passlib.context import CryptContext
# from datetime import datetime, timedelta
# from fastapi.staticfiles import StaticFiles
from app.users import routes as userRoutes

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

# app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(userRoutes.router)

@app.get("/")
def ack():
    return {"message": "Hello World!!!"}
