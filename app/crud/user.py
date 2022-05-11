from sqlalchemy.orm import Session
from app.database import Base
from typing import TypeVar, Optional
from app.crud.base import CRUDBase
from app.schema.User import UserCreate, UserUpdate
from app.schema.Login import Login
from app.models.models import Usuario

ModelType = TypeVar("ModelType", bound=Base)


class CRUDUser(CRUDBase[Usuario, UserCreate, UserUpdate]):

    def login(self, db: Session, *, obj_in: Login) -> ModelType:
        return db.query(self.model).filter(self.model.email == obj_in.email, self.model.senha == self.model.senha).first()
   

user = CRUDUser(Usuario)