from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.schema.Question import QuestionCreate, QuestionUpdate
from app.models.models import Pergunta

class CRUDQuestions(CRUDBase[Pergunta, QuestionCreate, QuestionUpdate]):
   pass

question = CRUDQuestions(Pergunta)