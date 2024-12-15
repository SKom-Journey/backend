from pydantic import BaseModel, Field
from typing import Optional

class Category(BaseModel):
    id: str = Optional[str]
    name: str = Field(...)
    total_menu: Optional[int] = Field(default=0)
    created_at: str = Field(...)