from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schema import Question as SchemaQuestion
from app.crud.question import question
from app.api import deps

router = APIRouter()


@router.get("", response_model=List[SchemaQuestion.Question])
def read_questions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    questions = question.get_multi(db=db, skip=skip, limit=limit)
    return questions


@router.post("", response_model=SchemaQuestion.Question)
def create_question(
    *,
    db: Session = Depends(deps.get_db),
    question_in: SchemaQuestion.QuestionCreate,
) -> Any:
    item = question.create(db=db, obj_in=question_in)
    return item

@router.put("/{id}", response_model=SchemaQuestion.Question)
def update_question(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    question_in: SchemaQuestion.QuestionUpdate,
) -> Any:
    item = question.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="question not found")
    item = question.update(db=db, db_obj=item, obj_in=question_in)
    return item

@router.delete("/{id}", response_model=SchemaQuestion.Question)
def delete_question(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    item = question.get(db=db, id=id)
    if not item:
        raise HTTPException(status_code=404, detail="question not found")
    question.remove(db=db, id=item.id)
    return item
