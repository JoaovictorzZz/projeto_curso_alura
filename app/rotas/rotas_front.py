from fastapi import APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.dependencias import RepoCliente
#ROTAS FRONT
router_front = APIRouter(
    prefix="/clientes"
)
templates = Jinja2Templates(directory='templates')
#exibi todos os clientes
@router_front.get('/', response_class=HTMLResponse)
async def exibir_clientes(request:Request, repo:RepoCliente):
    cliente = await repo.listar_cliente()
    return templates.TemplateResponse(
        request=request,
        name="clientes.html",
        context={"clientes" :cliente}
    )
#exibir o criar cliente
@router_front.get('/novo', response_class=HTMLResponse)
async def exibir_criar_cliente(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="clientes-form.html"
    )
#exibir o mostrar detalhes do cliente
@router_front.get("/{cliente_id}", response_class=HTMLResponse)
async def editar_detalhes(cliente_id:int,request:Request,repo:RepoCliente):
    cliente = await repo.obter_cliente(cliente_id)
    return templates.TemplateResponse(
        request=request,
        name="clientes-form.html",
        context={"cliente":cliente}
    )
