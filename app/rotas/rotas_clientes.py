from typing import Annotated
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

#utilizando o Router para uma nova rota fora da main principal 
from fastapi import APIRouter
from app.modelos.cliente import Cliente,ClienteCriar
from app.dependencias import RepoCliente

#ROTAS CLIENTES
router_clientes = APIRouter(
    prefix="/api/clientes"
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
@router_clientes.put('/{cliente_id}', response_model= Cliente)
async def atualiza_cliente(cliente_id:int,cliente:ClienteCriar,repo:RepoCliente):
    return await repo.atualizar_cliente(cliente_id,cliente)

