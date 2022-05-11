from fastapi import APIRouter

from app.api.api_v1.endpoints import user,question, answer, login


api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(user.router, prefix="/user", tags=["Usuários"])
api_router.include_router(question.router, prefix="/question", tags=["Questões"])
api_router.include_router(answer.router, prefix="/answer", tags=["Respostas"])
