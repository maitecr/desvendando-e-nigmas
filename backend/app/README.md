# BACKEND

As seguintes instruções de instalação e execução **devem ser feitas dentro do diretório backend**!

## Requisitos
* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [uvicorn](https://uvicorn.dev/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [PyMySQL](https://pypi.org/project/PyMySQL/)

## Preparação do ambiente
* Instalar `uv`
* Criar Ambiente Virtual
```
uv venv
```
* Excutar comando:
```
uv pip install -r requirements.txt
```

### NOTA 
Ao executar o comando `uv pip install -r requirements.txt`, deve ter sido instalado as dependências:
* FatAPI
* Uvicorn
* SQLAlchemy
* PyMySQL
* Alembic
* Pydantic
* Websockets

## Executar backend
* Em um terminal CLI, dentro do diretório `backend`:
```
uv run fastapi dev app/main.py
```
* Acessar a URL: 
```
http://localhost:8000
```
* Documentação automática gerada pela FastAPI: 
```
http://localhost:8000/docs
```