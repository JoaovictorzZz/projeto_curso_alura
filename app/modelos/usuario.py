from pydantic import BaseModel
class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str | None = None
# usuario criar
class CriarUsuario(BaseModel):
    nome: str
    email: str
    senha: str
