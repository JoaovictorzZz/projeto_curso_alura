from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependencias import RepoUsuario
from app.modelos.usuario import CriarUsuario


router_registro = APIRouter(prefix="/registro")
templates = Jinja2Templates(directory="templates")


# Exibir formulário de registro
@router_registro.get("/", response_class=HTMLResponse)
async def exibir_registro(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="registro.html"
    )


# Registrar usuário
@router_registro.post("/", response_class=HTMLResponse)
async def registrar_usuario(
    repo: RepoUsuario,
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    confirma_senha: str = Form(...)
):
    data = {
        "nome": nome,
        "email": email,
        "senha": senha,
        "confirma_senha": confirma_senha
    }

    if not all([nome, email, senha, confirma_senha]):
        return templates.TemplateResponse(
            request=request,
            name="registro.html",
            context={"erro": "Preencha todos os campos", **data}
        )

    if senha != confirma_senha:
        return templates.TemplateResponse(
            request=request,
            name="registro.html",
            context={"erro": "As senhas não coincidem", **data}
        )

    usuario_existente = await repo.buscar_email_usuario(email)

    if usuario_existente:
        return templates.TemplateResponse(
            request=request,
            name="registro.html",
            context={"erro": "Este e-mail já está cadastrado", **data}
        )

    usuario_criar = CriarUsuario(
        nome=nome,
        email=email,
        senha=senha
    )

    usuario = await repo.criar_usuarios(usuario_criar)

    if usuario:
        return RedirectResponse(
            url="/login",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="registro.html",
        context={"erro": "Não foi possível criar o usuário", **data}
    )
