#utilizando o Router para uma nova rota fora da main principal 
from fastapi import APIRouter
from app.modelos.cliente import Cliente
#Criando uma instância do Router
router = APIRouter(
    prefix="/clientes"
)
#rota do router tipo get  - indicando que vai retornar uma lista nao uma string qualquer
@router.get('/', response_model= list[Cliente])
async def buscar_clientes():
    lista = [Cliente(nome="Hugo", email="hugisss@gmail.com", telefone="99999992"),
             Cliente(nome="Leticia", email="lee@gmail.com", telefone="88888992")]
    return lista