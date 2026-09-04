from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.auth import obter_usuario_atual
from app.database import get_db
from app.db_models import UsuarioDB, TransacaoDB
from app.calculos import calcular_preco_medio


router = APIRouter()


@router.get("/ativos/{ticker}")
async def buscar_ativo(
    ticker: str,
    usuario_atual: UsuarioDB = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    ticker_formatado = ticker.upper()

    transacoes = db.query(TransacaoDB).filter(
        TransacaoDB.usuario_id == usuario_atual.id,
        TransacaoDB.ticker == ticker_formatado
    ).order_by(TransacaoDB.data).all()

    quantidade_atual, preco_medio_atual = calcular_preco_medio(transacoes)

    if quantidade_atual == 0:
        raise HTTPException(status_code=404, detail="Ativo não encontrado")

    return {
        "ticker": ticker_formatado,
        "quantidade": quantidade_atual,
        "preco_medio": round(preco_medio_atual, 2)
    }


@router.get("/ativos")
async def listar_ativos(usuario_atual: UsuarioDB = Depends(obter_usuario_atual), db: Session = Depends(get_db)):
    """Retorna quantidade e preço médio de cada ativo do usuário, calculados a partir do histórico de transações."""
    transacoes = db.query(TransacaoDB).filter(
        TransacaoDB.usuario_id == usuario_atual.id
    ).order_by(TransacaoDB.ticker, TransacaoDB.data).all()

    grupos = {}
    for transacao in transacoes:
        if transacao.ticker not in grupos:
            grupos[transacao.ticker] = []
        grupos[transacao.ticker].append(transacao)

    ativos = []
    for ticker, transacoes_do_ticker in grupos.items():
        quantidade, preco_medio = calcular_preco_medio(transacoes_do_ticker)
        if quantidade > 0:
            ativos.append({
                "ticker": ticker,
                "quantidade": quantidade,
                "preco_medio": round(preco_medio, 2)
            })

    return ativos