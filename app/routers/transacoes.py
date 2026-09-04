from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from app.models import TransacaoCriar
from app.db_models import TransacaoDB, UsuarioDB
from app.database import get_db
from app.auth import obter_usuario_atual

router = APIRouter(prefix="/transacoes", tags=["Transações"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_transacao(
    transacao: TransacaoCriar,
    usuario_atual: UsuarioDB = Depends(obter_usuario_atual),
    db: Session = Depends(get_db)
):
    ticker_formatado = transacao.ticker.strip().upper()

    nova_transacao = TransacaoDB(
        ticker=ticker_formatado,
        quantidade=transacao.quantidade,
        preco=transacao.preco,
        tipo=transacao.tipo,
        usuario_id=usuario_atual.id
    )

    db.add(nova_transacao)
    db.commit()
    db.refresh(nova_transacao)

    return {
        "status": "Transação criada com sucesso",
        "id": nova_transacao.id,
        "ticker": nova_transacao.ticker,
        "usuario": usuario_atual.username
    }