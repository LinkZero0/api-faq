from typing import Optional, Any
from pydantic import BaseModel

# Shared properties
class UserBase(BaseModel):
    nome: str = None
    email: str = None
    senha: str = None


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserInDBBase(UserUpdate):
    class Config:
        orm_mode = True

class User(UserInDBBase):
    id: int
    perguntas: Optional[Any]
    respostas: Optional[Any]
    pass

class UserInDB(UserInDBBase):
    pass