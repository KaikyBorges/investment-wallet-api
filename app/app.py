from app.routers import ativos, usuarios,transacoes
from fastapi import FastAPI
from app.routers import precos, carteira

#Base.metadata.create_all(bind=engine)

#Rotas importantes
app = FastAPI()
app.include_router(ativos.router)
app.include_router(usuarios.router)
app.include_router(transacoes.router)
app.include_router(precos.router)
app.include_router(carteira.router)