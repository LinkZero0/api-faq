from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema import Login as SchemaLogin
from app.crud.user import user
from app.api import deps

router = APIRouter()



@router.post("")
def login(
    *,
    db: Session = Depends(deps.get_db),
    user_in: SchemaLogin.Login,
) -> Any:
    item = user.login(db=db, obj_in=user_in)
    if not item:
        raise HTTPException(404, "Login não encontrado")
    return {"detail": "Logado com sucesso"}

