from sqlalchemy import Column, String
from .db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    cpf = Column(String)
    cargo = Column(String)
    perfil = Column(String)
    status = Column(String)
    imagem_url = Column(String)
    senha_hash = Column(String)

