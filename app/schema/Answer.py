from typing import Optional
from pydantic import BaseModel

# Shared properties
class AnswerBase(BaseModel):
    autor_id: int = None
    pergunta_id: int = None
    texto_resposta: str = None
    imagem: str = None


class AnswerCreate(AnswerBase):
    pass

class AnswerUpdate(AnswerBase):
    pass

class AnswerInDBBase(AnswerUpdate):
    class Config:
        orm_mode = True

class Answer(AnswerInDBBase):
    pass

class AnswerInDB(AnswerInDBBase):
    pass