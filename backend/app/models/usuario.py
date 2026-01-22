from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Usuario(Base):
    __tablename__ = "tb_usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement="auto")
    nm_usuario = Column(String(50), nullable=False, unique=True)
    nm_username = Column(String(16), nullable=False)
    dsc_email = Column(String(30), nullable=False, unique=True)
    pw_senha = Column(String(16), nullable=False)
    st_partida = Column(Boolean, nullable=False, default=False)


    # Relação Mãe-Filha
    usuario_como_proprietario = relationship(
        "ListaContato",
        foreign_keys="ListaContato.id_proprietario",
        back_populates="proprietario",
        cascade="all, delete-orphan"
    )

    usuario_como_anfitriao = relationship(
        "Partida",
        foreign_keys="Partida.id_anfitriao",
        back_populates="anfitriao",
        cascade="all, delete-orphan"
    )

    usuario_como_convidado = relationship(
        "Partida",
        foreign_keys="Partida.id_convidado",
        back_populates="convidado",
        cascade="all, delete-orphan"
    )

    autor_do_enigma = relationship(
        "Enigma",
        foreign_keys="Enigma.id_autor",
        back_populates="autoria",
        cascade="all, delete-orphan"
    )

    enviada_pelo_usuario = relationship(
        "Mensagem",
        foreign_keys="Mensagem.id_usuario",
        back_populates="enviada_pelo_usuario",
        cascade="all, delete-orphan"
    )