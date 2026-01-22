from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Lista_Contato(Base):
    __tablename__ = "tb_lista_contato"

    id_proprietario = Column(Integer, ForeignKey("tb_usuario.id_usuario"), nullable=False)
    id_contato = Column(Integer, ForeignKey("tb_usuario.id_usuario"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id_proprietario', 'id_contato'),
    )


    # Relação Filha-Mãe
    proprietario = relationship(
        "Usuario",
        foreign_keys=[id_proprietario],
        back_populates="usuario_como_proprietario"
    )
