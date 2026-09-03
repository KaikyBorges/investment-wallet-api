from app.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime


class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    senha_hash = Column(String)


class AtivoDB(Base):
    __tablename__ = "ativos"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    quantidade = Column(Integer)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

class TransacaoDB(Base):
    __tablename__="transacoes"

    id = Column(Integer,primary_key=True,index=True)
    ticker =Column(String, index=True)
    quantidade = Column(Integer)
    tipo= Column(String, index=True)
    preco = Column(Float)
    data = Column(DateTime, default=datetime.utcnow)
    usuario_id =Column(Integer,ForeignKey("usuarios.id"))
