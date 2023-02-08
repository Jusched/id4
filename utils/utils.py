# FastAPI
from fastapi import HTTPException

# bcrypt
import bcrypt

# PyJWT
import jwt

# Local modules
from models.users import User


def encrypt_password(password):
    """Encrypts the user's password to avoid
    dumping it as plain-text in the db."""

    salt = bcrypt.gensalt()
    password = password.encode("utf-8")
    hash_password = bcrypt.hashpw(password, salt)
    return hash_password


def check_password(db, user):
    """Checks if the given password checks with
    the encripted password in the db."""

    db_password = db.query(User).filter(User.email == user.email).first()
    if not db_password:
        raise HTTPException(400, "Email not found in database.")
    db_password.password.encode("utf-8")
    user.password.encode("utf-8")
    return bcrypt.checkpw(db_password.password, user.password)
    

def generate_token(email, secret):
    """Generates a JWT token to authenticate and logout user."""

    token = jwt.encode({"user": email}, secret, algorithm="HS256")
    return token
