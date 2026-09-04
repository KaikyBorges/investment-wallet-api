from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models import UsuarioDB, TransacaoDB, PrecoAtualDB
from app.auth import obter_usuario_atual
from app.calculos import calcular_resumo_carteira

router = APIRouter()


@router.get("/carteira/resumo")
async def resumo_carteira(
    usuario_atual: UsuarioDB = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    """Retorna patrimônio total, total investido, resultado e rentabilidade da carteira."""
    transacoes = db.query(TransacaoDB).filter(
        TransacaoDB.usuario_id == usuario_atual.id
    ).order_by(TransacaoDB.ticker, TransacaoDB.data).all()

    precos = db.query(PrecoAtualDB).all()
    precos_atuais = {p.ticker: p.preco for p in precos}

    return calcular_resumo_carteira(transacoes, precos_atuais)