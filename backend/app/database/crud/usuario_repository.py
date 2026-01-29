from sqlalchemy import select
import app.models as model

class UsuarioRepository:

    def read(self, db):
        stmt = select(model.Usuario)
        return db.scalars(stmt).all()