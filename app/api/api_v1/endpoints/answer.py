from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema import Answer as SchemaAnswer
from app.crud.answer import answer
from app.api import deps

router = APIRouter()


@router.get("", response_model=List[SchemaAnswer.Answer])
def read_answers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    answers = answer.get_multi(db=db, skip=skip, limit=limit)
    return answers


@router.post("", response_model=SchemaAnswer.Answer)
def create_answer(
    *,
    db: Session = Depends(deps.get_db),
    answer_in: SchemaAnswer.AnswerCreate,
) -> Any:
    item = answer.create(db=db, obj_in=answer_in)
    return item

@router.put("/{id}", response_model=SchemaAnswer.Answer)
def update_answer(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    answer_in: SchemaAnswer.AnswerUpdate,
) -> Any:
    item = answer.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="answer not found")
    item = answer.update(db=db, db_obj=item, obj_in=answer_in)
    return item

@router.delete("/{id}", response_model=SchemaAnswer.Answer)
def delete_answer(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    item = answer.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="answer not found")
    answer.remove(db=db, id=item.id)
    return item
