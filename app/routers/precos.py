from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models import UsuarioDB, PrecoAtualDB
from app.models import PrecoAtualizar
from app.auth import obter_usuario_atual

router = APIRouter()


@router.put("/precos/{ticker}")
async def atualizar_preco(
    ticker: str,
    preco_atualizar: PrecoAtualizar,
    usuario_atual: UsuarioDB = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    """Cria ou atualiza o preço atual de um ticker (upsert)."""
    ticker_formatado = ticker.upper()
    preco_db = db.query(PrecoAtualDB).filter(PrecoAtualDB.ticker == ticker_formatado).first()

    if preco_db:
        preco_db.preco = preco_atualizar.preco
        db.commit()
        return {"status": "Preço atualizado", "ticker": ticker_formatado, "preco": preco_db.preco}

    novo_preco = PrecoAtualDB(ticker=ticker_formatado, preco=preco_atualizar.preco)
    db.add(novo_preco)
    db.commit()
    return {"status": "Preço cadastrado", "ticker": ticker_formatado, "preco": novo_preco.preco}


@router.get("/precos/{ticker}")
async def buscar_preco(
    ticker: str,
    usuario_atual: UsuarioDB = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    """Consulta o preço atual de um ticker."""
    ticker_formatado = ticker.upper()
    preco_db = db.query(PrecoAtualDB).filter(PrecoAtualDB.ticker == ticker_formatado).first()

    if not preco_db:
        return {"ticker": ticker_formatado, "preco": None, "status": "Preço não cadastrado"}

    return {"ticker": ticker_formatado, "preco": preco_db.preco}