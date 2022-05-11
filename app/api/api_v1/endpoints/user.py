from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema import User as SchemaUser
from app.crud.user import user
from app.api import deps

router = APIRouter()


@router.get("", response_model=List[SchemaUser.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    users = user.get_multi(db=db, skip=skip, limit=limit)
    return users


@router.post("", response_model=SchemaUser.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: SchemaUser.UserCreate,
) -> Any:
    item = user.create(db=db, obj_in=user_in)
    return item

@router.put("/{id}", response_model=SchemaUser.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    user_in: SchemaUser.UserUpdate,
) -> Any:
    item = user.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="user not found")
    item = user.update(db=db, db_obj=item, obj_in=user_in)
    return item

@router.delete("/{id}", response_model=SchemaUser.User)
def delete_user(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    item = user.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="user not found")
    user.remove(db=db, id=item.id)
    return item
