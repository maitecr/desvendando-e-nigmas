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
    
    
    # Relação Mãe-Filha
    usuario_como_proprietario = relationship(
        "Lista_Contato",
        foreign_keys="Lista_Contato.id_proprietario",
        back_populates="proprietario",
    )

    usuario_como_anfitriao = relationship(
        "Partida",
        foreign_keys="Partida.id_anfitriao",
        back_populates="anfitriao",
    )

    usuario_como_convidado = relationship(
        "Partida",
        foreign_keys="Partida.id_convidado",
        back_populates="convidado",
    )

    autor_do_enigma = relationship(
        "Enigma",
        foreign_keys="Enigma.id_autor",
        back_populates="autoria",
    )

    mensagens_do_usuario = relationship(
        "Mensagem",
        foreign_keys="Mensagem.id_usuario",
        back_populates="enviada_pelo_usuario",
    )
