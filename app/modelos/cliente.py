#classe cliente
# Pydantic: biblioteca usada para criar modelos e validar os dados que entram e saem da API.
from pydantic import BaseModel
class Cliente(BaseModel):
    id_:int | None
    nome:str
    email:str
    telefone:str
class ClienteCriar(BaseModel):
    nome:str
    email:str
    telefone:str



