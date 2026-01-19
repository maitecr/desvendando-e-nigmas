# Importando o FastAPI
from fastapi import FastAPI

# Criando uma instância do FastAPI
app = FastAPI()

# Criando nossa primeira rota
# O decorador @app.get("/") diz: "quando alguém acessar a raiz da API, execute esta função"
@app.get("/")
def raiz():
    return {"mensagem": "Testando inicialização de projeto FastAPI"}
