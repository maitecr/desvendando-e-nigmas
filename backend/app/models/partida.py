from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Partida(Base):
    __tablename__ = "tb_partida"

    id_partida = Column(Integer, primary_key=True, autoincrement="auto")
    dt_inicio = Column(DateTime, nullable=False, server_default=func.now())
    dt_fim = Column(DateTime, nullable=True)
    id_enigma = Column(Integer, ForeignKey("tb_enigma.id_enigma"), nullable=False)
    id_anfitriao = Column(Integer, ForeignKey("tb_usuario.id_usuario"), nullable=False)
    id_convidado = Column(Integer, ForeignKey("tb_usuario.id_usuario"), nullable=False)

    # Relação Filha-Mãe    
    enigma = relationship(
        "Enigma",
        foreign_keys=[id_enigma],
        back_populates=["enigma_na_partida"]
    )

    anfitriao = relationship(
        "Usuario",
        foreign_keys=[id_anfitriao],
        back_populates="usuario_como_anfitriao"
    )

    convidado = relationship(
        "Usuario",
        foreign_keys=[id_convidado],
        back_populates="usuario_como_convidado"
    )

    # Relação Mãe-Filha
    mensagem_da_partida = relationship(
        "Mensagem",
        foreign_keys=["Mensagem.id_mensagem"],
        back_populates="mensagem_na_partida",
        cascade="all, delete-orphan"
    )