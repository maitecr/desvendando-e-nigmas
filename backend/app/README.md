# BACKEND

InstruçÕes de instalação e execução do backend.

## Requisitos
* uv manager: [instalação](https://docs.astral.sh/uv/getting-started/installation/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [uvicorn](https://uvicorn.dev/)

## Preparação do ambiente
* Instalar `uv`
* Instalar FastAPI:
```
uv pip install 'fastapi[standart]'
```
* Instalar uvicorn:
```
uv pip install uvicorn
```

## Executar backend
* Em um terminal CLI, dentro do diretório `backend`:
```
uv run fastapi dev app/main.py
```
* Acessar a URL: `http://localhost:8000`
* Documentação automática gerada pela FastAPI: `http://localhost:8000/docs`