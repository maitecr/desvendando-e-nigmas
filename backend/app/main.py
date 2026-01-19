from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.connection import engine
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    engine.dispose()  

app = FastAPI(lifespan=lifespan)

@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "conectado"}
    except Exception as e:
        return {"db": "erro", "detalhe": str(e)}

@app.get("/")
def raiz():
    return {"mensagem": "Testando inicialização de projeto FastAPI"}
