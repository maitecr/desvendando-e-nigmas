from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base
from app.models.partida import Partida

class Enigma(Base):
    __tablename__ = "tb_enigma"

    id_enigma = Column(Integer, primary_key=True, autoincrement="auto")
    txt_titulo = Column(String(50), nullable=False)
    txt_descricao = Column(String(100), nullable=False)
    id_autor = Column(Integer, ForeignKey("tb_usuario.id_usuario"))

    # Relação Filha-Mãe
    autoria = relationship(
        "Usuario",
        foreign_keys=[id_autor],
        back_populates="autor_do_enigma"
    )

    # Relação Mãe-Filha 
    enigma_na_partida = relationship(
        "Partida",
        back_populates="enigma",
    )