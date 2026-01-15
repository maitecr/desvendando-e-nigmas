# Importando o FastAPI
from fastapi import FastAPI

# Criando uma instância do FastAPI
# Esta será a base da nossa aplicação
app = FastAPI()


# Criando nossa primeira rota
# O decorador @app.get("/") diz: "quando alguém acessar a raiz da API, execute esta função"
@app.get("/")
def raiz():
    """Rota raiz - retorna uma mensagem de boas-vindas"""
    return {"mensagem": "Testando inicialização de projeto FastAPI"}


# Para rodar esta API, execute no terminal (a partir da raiz do projeto):
# uv run fastapi dev app/main.py
#
# Depois acesse no navegador:
# http://localhost:8000
#
# Para ver a documentação automática:
# http://localhost:8000/docs