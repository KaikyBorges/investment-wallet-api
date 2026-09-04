# Investment Wallet API

> REST API para gerenciamento e acompanhamento de uma carteira de investimentos, desenvolvida com foco em arquitetura de back-end, persistência de dados, autenticação e organização por recursos.

## Sobre o projeto

O **Investment Wallet API** é um projeto de estudo voltado à construção de uma API REST com Python. A aplicação organiza usuários, ativos, transações, preços e informações consolidadas da carteira em recursos separados.

O projeto foi estruturado para evoluir gradualmente de uma API simples para uma aplicação de back-end mais próxima de um sistema real, mantendo separação de responsabilidades e controle de alterações no banco de dados.

## Principais recursos

- Cadastro e gerenciamento de usuários
- Autenticação baseada em JWT
- Proteção de rotas com dependências do FastAPI
- Cadastro e consulta de ativos
- Registro de transações
- Consulta de preços
- Cálculos relacionados à carteira
- Persistência com SQLAlchemy
- Migrações de banco com Alembic
- Validação de dados com Pydantic
- Configuração por variáveis de ambiente

## Stack

| Tecnologia | Uso |
| --- | --- |
| Python | Linguagem principal |
| FastAPI | Framework da API REST |
| Pydantic | Validação e schemas |
| SQLAlchemy | ORM e persistência |
| Alembic | Migrações do banco |
| SQLite | Banco de dados para desenvolvimento |
| JWT / python-jose | Autenticação |
| bcrypt | Hash de senhas |
| Uvicorn | Servidor ASGI |
| python-dotenv | Configuração por ambiente |

## Arquitetura

```text
investment-wallet-api/
├── app/
│   ├── app.py              # Inicialização da aplicação FastAPI
│   ├── auth.py             # Autenticação e usuário atual
│   ├── calculos.py         # Regras e cálculos da carteira
│   ├── config.py           # Configurações da aplicação
│   ├── database.py         # Conexão e sessão do banco
│   ├── db_models.py        # Modelos SQLAlchemy
│   ├── models.py           # Schemas Pydantic
│   └── routers/
│       ├── ativos.py       # Endpoints de ativos
│       ├── carteira.py     # Endpoints consolidados da carteira
│       ├── precos.py       # Endpoints de preços
│       ├── transacoes.py   # Endpoints de transações
│       └── usuarios.py     # Endpoints de usuários e autenticação
├── alembic/                # Histórico de migrações
├── docs/                   # Documentação complementar
├── alembic.ini
├── requirements.txt
└── README.md
```

## Fluxo da aplicação

```text
Cliente
   │
   ▼
FastAPI
   │
   ├── Routers
   │      ├── Usuários
   │      ├── Ativos
   │      ├── Transações
   │      ├── Preços
   │      └── Carteira
   │
   ▼
Regras de negócio
   │
   ▼
SQLAlchemy
   │
   ▼
Banco de dados
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/KaikyBorges/investment-wallet-api.git
cd investment-wallet-api
```

### 2. Crie um ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
```

Não versionar o `.env`. Ele deve permanecer protegido pelo `.gitignore`.

### 5. Execute as migrações

```bash
alembic upgrade head
```

### 6. Inicie a API

```bash
uvicorn app.app:app --reload
```

A documentação interativa ficará disponível no ambiente local em `/docs`, e a documentação alternativa em `/redoc`.

## Autenticação

A API utiliza tokens JWT para autenticar usuários. As rotas protegidas utilizam uma dependência responsável por validar o token e recuperar o usuário correspondente no banco.

> Para produção, chaves secretas devem ser fornecidas por um mecanismo seguro de gerenciamento de configuração/segredos e nunca pelo código-fonte.

## Banco de dados e migrações

O projeto utiliza **SQLAlchemy** como camada ORM e **Alembic** para versionar alterações estruturais no banco.

Comandos principais:

```bash
alembic upgrade head
alembic current
alembic history
```

## Objetivos de evolução

- [ ] Cobertura de testes automatizados com pytest
- [ ] Testes de integração dos endpoints
- [ ] Separação mais clara entre routers, services e repositories
- [ ] Melhor tratamento de erros e respostas padronizadas
- [ ] PostgreSQL para ambiente de produção
- [ ] Docker e Docker Compose
- [ ] CI com GitHub Actions
- [ ] Deploy da API
- [ ] Observabilidade e logging estruturado
- [ ] Documentação completa dos endpoints e exemplos de payloads

## Status

**Em desenvolvimento.** O projeto está sendo construído de forma incremental como projeto de portfólio e estudo de desenvolvimento back-end.

## Autor

**Kaiky Borges** — estudante de Ciência de Dados e desenvolvedor back-end em formação.

- GitHub: https://github.com/KaikyBorges
- Perfil: https://github.com/KaikyBorges/KaikyBorges

## Licença

Este projeto está disponível para fins educacionais e de portfólio.
