from enum import Enum
from pydantic import BaseModel

class UsuarioCadastro(BaseModel):
    username: str
    senha: str


class TipoTransacao(str, Enum):
    COMPRA = "COMPRA"
    VENDA = "VENDA"

class TransacaoCriar(BaseModel):
    ticker: str
    tipo: TipoTransacao
    quantidade: int
    preco: float


class PrecoAtualizar(BaseModel):
    preco: float