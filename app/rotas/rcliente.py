#utilizando o Router para uma nova rota fora da main principal 
from fastapi import APIRouter
from app.modelos.cliente import Cliente
#Criando uma instância do Router
router = APIRouter(
    prefix="/clientes"
)
lista = [Cliente(id_=1,nome="Hugo", email="hugisss@gmail.com", telefone="99999992"),
             Cliente(id_=2, nome="Leticia", email="lee@gmail.com", telefone="88888992")]

#rota do router tipo get  - indicando que vai retornar uma lista nao uma string qualquer
#perceba que uso o response_model
@router.get('/', response_model= list[Cliente])
async def buscar_clientes():
    return lista

@router.get('/{cliente_id}',response_model=Cliente | None)
async def obter_cliente(cliente_id:int):
    for cliente in lista:
        if cliente.id_ == cliente_id:
            return cliente
    return None

@router.post('/criar')
async def criarU(cliente:Cliente):
    lista.append(cliente)
    return {
        "mensagem": 'usuario criado com sucesso',
        "cliente": cliente.nome
    }
