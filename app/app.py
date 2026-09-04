from fastapi import FastAPI

from app.routers import ativos, carteira, precos, transacoes, usuarios

app = FastAPI(
    title="Investment Wallet API",
    description="API REST para gerenciamento e acompanhamento de uma carteira de investimentos.",
    version="1.0.0",
)

app.include_router(ativos.router)
app.include_router(usuarios.router)
app.include_router(transacoes.router)
app.include_router(precos.router)
app.include_router(carteira.router)
