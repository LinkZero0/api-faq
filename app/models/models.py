from sqlalchemy import TEXT, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha = Column(String, nullable=False)

    perguntas = relationship("Pergunta", back_populates="autor")
    respostas = relationship("Resposta", back_populates="autor")


class Pergunta(Base):
    __tablename__ = "pergunta"

    id = Column(Integer, primary_key=True, index=True)
    autor_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    palavra_chave = Column(String, index=True, nullable=False)
    texto_pergunta = Column(TEXT, nullable=False)
    imagem = Column(TEXT)

    autor = relationship("Usuario", back_populates="perguntas")
    respostas = relationship("Resposta", back_populates="pergunta")


class Resposta(Base):
    __tablename__ = "resposta"

    id = Column(Integer, primary_key=True, index=True)
    autor_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    pergunta_id = Column(Integer, ForeignKey("pergunta.id"), nullable=False)
    texto_resposta = Column(TEXT, nullable=False)
    imagem = Column(TEXT)

    autor = relationship("Usuario", back_populates="respostas")
    pergunta = relationship("Pergunta", back_populates="respostas")
