#Importando o framework FastAPI, e Request(requisicao do usuario)
from fastapi import FastAPI,Request
# Jinja permite renderizar HTML com dados do Python
from fastapi.templating import Jinja2Templates
# Permite usar arquivos CSS, JS e imagens
from fastapi.staticfiles import StaticFiles
# Informa que a rota retorna HTML
from fastapi.responses import HTMLResponse
#
from app.rotas import rotas_clientes,rotas_front,rota_front_login

#Criando uma instância da aplicação
app = FastAPI(
    title='Techlog Solutions API',
    description='CRM para Techlog Solutions',
    version='1.0.0',
)
# Define a pasta onde ficam os HTMLs
templates = Jinja2Templates(directory='templates')
# Disponibiliza CSS, JS e imagens da pasta static
app.mount("/static",StaticFiles(directory="static"), name="static")
#importando e incluindo nossa rotas Router
app.include_router(rotas_clientes.router_clientes)
app.include_router(rotas_front.router_front)
app.include_router(rota_front_login.router_login)

##rotas
#padrao de mercado - vereficar status da  api 
@app.get('/health')
async def health_check():
     return {"status": "OK"}
#
@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse(
         request=request,
         name="index.html",
         context={"titulo":"Techlog Solutions", "versao":"1.0.0"}
    )
 