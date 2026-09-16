from typing import Annotated
#utilizando o Router para uma nova rota fora da main principal 
from fastapi import APIRouter,Depends,HTTPException
from app.modelos.cliente import Cliente
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import obter_cliente_repositorio

#Criando uma instância do Router
router_clientes = APIRouter(
    prefix="/clientes"
)

#rota do router tipo get  - indicando que vai retornar uma lista nao uma string qualquer
#perceba que uso o response_model
@router_clientes.get('/', response_model= list[Cliente])
async def buscar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_cliente()

#obter cliente por ID
@router_clientes.get('/{cliente_id}',response_model=Cliente | None)
async def obter_cliente(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)], cliente_id:int):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Erro: cliente não encontrado")
    return cliente
    
#criar cliente
@router_clientes.post('/criar')
async def criarU(cliente:Cliente):
    lista.append(cliente)
    return {
        "mensagem": 'usuario criado com sucesso',
        "cliente": cliente.nome
    }
