import bcrypt
#importação para criptografar as senhas dos usuarios
from fastapi import APIRouter, HTTPException,Depends
#instalar dependencias para outros arquivos
from jose import jwt
#cria um token para cada requisição ao tentar interagir
from datetime import datetime, timedelta

from app.models import UsuarioCadastro
#import o modelo pydantic para entrada de dados no banco
from app.config import SECRET_KEY, ALGORITHM
#importa a SECRET_KEY para ser utilizada no banco de dados original
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models import UsuarioDB
#importações basicas para a utilização do sqlalchemy

#inicia as rotas para o projeto
router = APIRouter()

#rota para cadastrar e verificar os usuarios ja existentes dentro do banco de dados
@router.post("/usuarios")
async def cadastrar_usuarios(usuario: UsuarioCadastro, db: Session = Depends(get_db)):
    usuario_existente = db.query(UsuarioDB).filter(UsuarioDB.username == usuario.username).first()
    if usuario_existente:
        raise HTTPException(status_code=409, detail="Usuário já existe")

    user_hash = bcrypt.hashpw(usuario.senha.encode('utf-8'), bcrypt.gensalt())

    novo_usuario = UsuarioDB(username=usuario.username, senha_hash=user_hash)
    db.add(novo_usuario)
    db.commit()

    return {"status": "usuário cadastrado", "username": usuario.username}

from fastapi.security import OAuth2PasswordRequestForm

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.username == form_data.username).first()
    if not usuario:
        raise HTTPException(401, "Usuário ou senha incorretos")

    senha_valida = bcrypt.checkpw(form_data.password.encode('utf-8'), usuario.senha_hash)
    if not senha_valida:
        raise HTTPException(401, "Usuário ou senha incorretos")

    expira_em = datetime.utcnow() + timedelta(minutes=30)
    token = jwt.encode({"sub": form_data.username, "exp": expira_em}, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}