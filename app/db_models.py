from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime


class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    senha_hash = Column(String)


class TransacaoDB(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    quantidade = Column(Integer)
    tipo = Column(String, index=True)
    preco = Column(Float)
    data = Column(DateTime, default=datetime)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

class PrecoAtualDB(Base):
    __tablename__ = "precos_atuais"

    ticker = Column(String, primary_key=True)
    preco = Column(Float, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)