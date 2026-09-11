#classe cliente
# Pydantic: biblioteca usada para criar modelos e validar os dados que entram e saem da API.
from pydantic import BaseModel

class Cliente(BaseModel):
    id_:int
    nome:str
    email:str
    telefone:str


c1 = Cliente(id_=4,nome="Joao", email="jjoao@gmail.com", telefone="15998554798")
# model_dump() -> transforma o modelo Pydantic em dicionário Python
# model_dump_json() -> serializa o modelo Pydantic para uma string JSON
exibindo = c1.model_dump_json()
print(exibindo)
