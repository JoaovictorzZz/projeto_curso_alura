from typing import Annotated

#utilizando o Router para uma nova rota fora da main principal 
from fastapi import APIRouter,Depends,HTTPException
from app.modelos.cliente import Cliente,ClienteCriar
from app.banco_de_dados.banco_local import BancoDeDadosLocal
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependencias import RepoCliente

#Criando uma instância do Router
router_clientes = APIRouter(
    prefix="/clientes"
)
#rota do router tipo get  - indicando que vai retornar uma lista nao uma string qualquer
#perceba que uso o response_model
@router_clientes.get('/', response_model= list[Cliente])
async def buscar_clientes(repo:RepoCliente):
    return await repo.listar_cliente()
#obter cliente por ID
@router_clientes.get('/{cliente_id}',response_model=Cliente | None)
async def obter_cliente(cliente_id:int,repo:RepoCliente):
    return await repo.obter_cliente(cliente_id)
#criar cliente
@router_clientes.post('/', response_model=ClienteCriar)
async def criar_cliente(cliente:ClienteCriar,repo:RepoCliente):
   return await repo.criar_cliente(cliente)
    
#excluir cliente
@router_clientes.delete('/{cliente_id}')
async def deletar_cliente(cliente_id:int, repo:RepoCliente):
    return await repo.remove_cliente(cliente_id)
#atualizar cliente
@router_clientes.put('/', response_model= Cliente | None )
async def atualiza_cliente(cliente:Cliente,repo:RepoCliente):
    return await repo.atualizar_cliente(cliente)
    