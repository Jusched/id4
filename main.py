# FastAPI
from fastapi import FastAPI, HTTPException, Response

# Local modules
import uuid
from models.users import User, UserIn
from config.database import Base, Session, engine
from utils.utils import encrypt_password

# Logger
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.FileHandler('api.log')
handler.setFormatter(formatter)

logger.addHandler(handler)


app = FastAPI()
app.title = "4ID Login/logout API"

Base.metadata.create_all(bind=engine)


@app.post("/signup", tags=["Signup"], response_model=dict, status_code=201)
def signup(user: UserIn):
    """Registers a new user in the database.
    
    Receives an email (unique) and a password.
    """

    logging.info("Starting Signup endpoint.")
    if len(user.password) < 8:
        logger.error("Exception: Password must be longer than 8 characters.")
        raise HTTPException(400, "Password must be longer than 8 characters.")
    
    
    db = Session()

    hash_password = encrypt_password(user.password)
    new_user = User(**user.dict())
    new_user.password, user.password = hash_password, hash_password
    new_user.session_id = str(uuid.uuid4())

    db.add(new_user)
    db.commit()
    logging.info("Signup endpoint completed.")
    return user


@app.post("/logout", tags=["Logout"], response_model=dict, status_code=200)
def logout(email: str):
    """Logs out the user based on provided email."""

    logging.debug(f"Received request to logout user with email: {email}")
    db = Session()
    user = db.query(User).filter(User.email == email).first()

    if not user:
        logging.debug(f"Exception: User with email: {email} not found.")
        raise HTTPException(400, "Email not found.")
    
    if not user.session_id:
        logging.debug(f"User with email: {email} already logged out.")
        raise HTTPException(400, "Exception: Email is already logged out.")
    
    user.session_id = None
    db.add(user)
    db.commit()
    logging.info(f"User with email: {email} successfully logged out.")
    return Response(content="Logged out successfully.", status_code=200)


@app.get("/clear", tags=["Database"],status_code=204)
def clear_db():
    """Deletes everything in the database
    and builds it up again."""

    logging.debug("Received request to clear database.")

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    logging.info("Database cleared and recreated successfully.")
    return 


