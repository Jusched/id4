# FastAPI
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

# Bcrypt
import bcrypt

# Local modules
from .models import User
from .config import Session, engine


app = FastAPI()


@app.post("/register")
def register(data: OAuth2PasswordBearer, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == data.username).first()

