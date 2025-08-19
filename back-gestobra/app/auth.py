from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from . import crud, schemas
from .db.database import SessionLocal
from .security import verificar_senha, criar_token, verificar_token

router = APIRouter()
""" oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") """

security = HTTPBearer()

def get_current_token(credentials = Depends(security)):
    token = credentials.credentials
    return token

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de login
@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = crud.buscar_usuario_por_email(db, form_data.username)
    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos")

    access_token = criar_token({"sub": usuario.nome})
    return {"access_token": access_token, "token_type": "bearer"}

# Dependência para proteger rotas
def usuario_atual(token: str = Depends(get_current_token), db: Session = Depends(get_db)):
    dados = verificar_token(token)
    if not dados:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido ou expirado")
    usuario = crud.buscar_usuario_por_nome(db, dados["sub"])
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Exemplo de rota protegida
@router.get("/perfil")
def perfil(usuario=Depends(usuario_atual)):
    return {"mensagem": f"Bem-vindo, {usuario.nome}!"}
