import os
from dotenv import load_dotenv

load_dotenv()  # carrega as variáveis do arquivo .env para o ambiente

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"