from sqlalchemy import select
import app.models as model

class UsuarioRepository:

    def get(self, db) -> list[model.Usuario] | None:
        stmt = select(model.Usuario)
        return db.scalars(stmt).all()
    
    def get_by_id(self, db, id_usuario) -> model.Usuario | None:
        return db.query(model.Usuario).filter(model.Usuario.id_usuario == id_usuario).first()

