from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.schema.Answer import AnswerCreate, AnswerUpdate
from app.models.models import Resposta

class CRUDAnswer(CRUDBase[Resposta, AnswerCreate, AnswerUpdate]):
   pass

answer = CRUDAnswer(Resposta)