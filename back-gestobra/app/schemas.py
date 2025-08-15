from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str
    telefone: str
    status: str

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioOut(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

class LoginData(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
