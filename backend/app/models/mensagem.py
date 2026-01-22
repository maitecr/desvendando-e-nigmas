from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Mensagem(Base):
    __tablename__ = "tb_mensagem"

    id_mensagem = Column(Integer, primary_key=True)
    dt_mensagem = Column(DateTime, nullable=False, server_default=func.now())
    txt_mensagem = Column(String(100), nullable=False)
    id_usuario = Column(Integer, ForeignKey("tb_usuario.id_usuario"), nullable=False)
    id_partida = Column(Integer, ForeignKey("tb_partida.id_partida"), nullable=False)

    # Relação Filha-Mãe
    enviada_pelo_usuario = relationship(
        "Usuario",
        foreign_keys=[id_usuario],
        back_populates="mensagem_do_usuario"
    )

    mensagem_na_partida = relationship(
        "Partida",
        foreign_keys=[id_partida],
        back_populates="mensagem_da_partida",
    )