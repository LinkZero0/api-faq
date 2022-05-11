from typing import Optional
from pydantic import BaseModel

# Shared properties
class QuestionBase(BaseModel):
    autor_id: int = None
    palavra_chave: str = None
    texto_pergunta: str = None
    imagem: str = None


class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    pass

class QuestionInDBBase(QuestionUpdate):
    class Config:
        orm_mode = True

class Question(QuestionInDBBase):
    pass

class QuestionInDB(QuestionInDBBase):
    pass