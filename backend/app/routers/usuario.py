from fastapi import APIRouter, Depends, HTTPException
from app.database.repository.usuario_repository import UsuarioRepository
from app.database.connection import get_db

router = APIRouter(prefix="/usuarios")

repository = UsuarioRepository()

@router.get("/")
def read(conn=Depends(get_db)):
    """ Rota para retornar todos os usuários registrados na tb_usuario """

    get_all_usuarios = repository.get(conn)

    if not get_all_usuarios:
        raise HTTPException(status_code=404, detail="Sem registro de usuários")

    return get_all_usuarios

@router.get("/{id_usuario}")
def read_user_by_id(id_usuario: int, conn=Depends(get_db)):
    """ Retornar usuário pelo campo id_usuario """

    get_usuario_by_id = repository.get_by_id(conn, id_usuario)

    if not get_usuario_by_id:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return get_usuario_by_id