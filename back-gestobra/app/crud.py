from sqlalchemy.orm import Session

from .modules.users import model
from . import schemas
from .security import gerar_hash_senha

def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    senha_hash = gerar_hash_senha(usuario.senha)
    db_usuario = model.Usuario(
        nome=usuario.nome, 
        email=usuario.email, 
        telefone=usuario.telefone, 
        status=usuario.status,
        senha_hash=senha_hash, 
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def listar_usuarios(db: Session):
    return db.query(model.Usuario).all()

def buscar_usuario_por_nome(db: Session, nome: str):
    return db.query(model.Usuario).filter(model.Usuario.nome == nome).first()

def buscar_usuario_por_email(db: Session, email: str):
    return db.query(model.Usuario).filter(model.Usuario.email == email).first()