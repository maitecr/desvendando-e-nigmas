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

### Quando incluir nova dependência ao projeto, executar o comando:
```
uv freeze > requirements
```

## Conectar com Banco de Dados usando PyMySQL
* No diretório `backend` criar o arquivo `.env`
* Incluir a constante `DATABASE_URL=mysql+pymysql://seu_usuario:sua_senha@localhost/nome_do_banco`

## Executar backend
* Em um terminal CLI, dentro do diretório `backend`:
```
uv run fastapi dev app/main.py
```

* Acessar a URL: 
```python
http://localhost:8000

# Deverá retornar o json "{"mensagem": "Testando inicialização de projeto FastAPI"}"
```

* Acessar a URL:
```python
http://127.0.0.1:8000/db-test

# Deverá retornar o json {"db":"conectado"}.
```

* Documentação automática gerada pela FastAPI: 
```
http://localhost:8000/docs
```

* Comando para encerrar a aplicação:
```
ctrl + c
```

 ### NOTA
 Até o momento apenas testamos se a aplicação é executada e se está conectando com o banco de dados MariaDB com PyMYSQL, mas ainda não há tabelas geradas. 

## Migrations com Alembic no MariaDB
* Estamos usando o UV para gerenciar pacotes, mas como o Alembic está instalado como dependência dentro do nosso ambiente virtual, devemos ativar o ambiente antes de iniciarmos as migrations com o comando:
```
.venv\Scripts\activate
```
* Para gerar as migrations no diretório `alembic/versions`:
```
alembic revision --autogenerate -m "sua mensagem aqui"
```
* Cria as tabelas das migrations no banco de dados:
```
alembic upgrade head
```
* Desativar o ambiente virtual antes de [iniciar a aplicação]():
```
.venv\Scripts\deactivate
```