# FastAPI
from fastapi import FastAPI, HTTPException

# Bcrypt
import bcrypt

# Local modules
from models.users import User, UserIn
from config.database import Base, Session, engine
from utils.utils import encrypt_password, check_password, generate_token



app = FastAPI()
app.title = "FastAPI login/logout API."

Base.metadata.create_all(bind=engine)


@app.post("/signup", tags=["Signup"], response_model=dict, status_code=201)
def signup(user: UserIn):
    """Registers a new user in the database.
    
    Receives an email (unique) and a password.
    """

    if len(user.password) < 8:
        raise HTTPException(400, "Password must be longer than 8 characters.")
    
    db = Session()

    hash_password = encrypt_password(user.password)
    new_user = User(**user.dict())
    new_user.password, user.password = hash_password, hash_password

    new_user.token = generate_token(new_user.email, new_user.password)
    db.add(new_user)
    db.commit()
    return user


@app.post("/login", tags=["Login"], response_model=dict, status_code=200)
def login(user: UserIn):
    """Logs in existing users."""

    db = Session()
    verified = check_password(db, user)


@app.post("/logout", tags=["Logout"], response_model=dict, status_code=200)
def logout(email: str):
    """Logs out the user based on provided email."""

    db = Session()
    result = db.query(User).filter(User.email == email).first()
    if not result:
        raise HTTPException(400, "Email not found in database.")
    db.delete(result)
    db.commit()
    return 


@app.get("/clear", tags=["Database"],status_code=204)
def clear_db():
    """Deletes everything in the database
    and builds it up again."""

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return 