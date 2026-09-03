from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.config import SECRET_KEY, ALGORITHM
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.db_models import UsuarioDB



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def obter_usuario_atual(token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        usuario_db =db.query(UsuarioDB).filter(UsuarioDB.username == username).first()
        if not usuario_db:
            raise HTTPException(status_code=401,detail="Usuario não encontrado ou não existente")
        # 3. se "sub" não existir por algum motivo, levantar HTTPException(401, ...)
        return usuario_db
    except JWTError:

        raise HTTPException(status_code=401, detail="Token inválido ou expirado")