# Pydantic
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    """User class for login/logout."""

    email: EmailStr = Field(max_length=30)
    hash_password: str

    

