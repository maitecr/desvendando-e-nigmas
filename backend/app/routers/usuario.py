from fastapi import APIRouter, Depends
from app.database.crud.usuario_repository import UsuarioRepository
from app.database.connection import get_db

router = APIRouter(prefix="/usuarios")

repository = UsuarioRepository()

@router.get("/")
def get_all_usuarios(conn=Depends(get_db)):
    return repository.read(conn)
