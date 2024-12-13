from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Session(BaseModel):
    id: str = Optional[str]
    access_token: str = Optional[str]
    type: str = Field(...)
    user_id: str = Field(...)
    created_at: str

class UserType(Enum):
    ADMIN = "ADMIN"
    USER = "USER"