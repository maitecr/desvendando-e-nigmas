from fastapi import APIRouter, Depends
import database as db

router = APIRouter(prefix="/usuarios")

repository = db.UsuarioRepository()

@router.get("/")
def get_all_usuarios(conn = Depends(db.get_db)):
    return repository.read(conn)



