# SQLAlchemy
from sqlalchemy import Column, Integer, String

# Database configuration.
from ..config import Base


class User(Base):
    """User class for login/logout."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    
