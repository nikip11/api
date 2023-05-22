from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
    name: str
    fullName: str
    password: Optional[str]
    
