from pydantic import BaseModel, Field
from typing import Optional
from models.Session import Session

class User(BaseModel):
    id: str = Optional[str]
    session: Session = Field(default=None)
    email: str = Field(...)
    password: str = Field(...)
    name: str = Field(...)
    with_google: bool = Field(default=False)
    created_at: str