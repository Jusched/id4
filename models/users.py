# SQLAlchemy
from sqlalchemy import Column, Integer, String

# Pydantic
from pydantic import BaseModel, EmailStr
from typing import Optional

# Database configuration.
from config.database import Base


class User(Base):
    """User class for database."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    

class UserIn(BaseModel):
    """User for authentication."""

    email: EmailStr
    password: str
    session_id : Optional[str] = None
    