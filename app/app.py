from app.routers import ativos, usuarios,transacoes
from fastapi import FastAPI
from app.database import engine, Base
from app import db_models

#Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(ativos.router)
app.include_router(usuarios.router)
app.include_router(transacoes.router)