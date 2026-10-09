from fastapi import APIRouter,Request,Form
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependencias import RepoUsuario
#ROTAS LOGIN 
router_login = APIRouter(
    prefix="/login"
)
#
templates = Jinja2Templates(directory="templates")
#
@router_login.get("/", response_class=HTMLResponse)
async def pagina_login(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
    )
#
@router_login.post("/",response_class=HTMLResponse)
async def login(repo:RepoUsuario, request:Request, email:str = Form(...),senha:str = Form(...)):
    usuario = await repo.buscar_usuarios_email_senha(email,senha)
    if usuario:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="session_token", value="token_senha", httponly=True)
        return response
    else:
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"email":email, "senha":senha, "error": "Credencias Invalidas"}
        )