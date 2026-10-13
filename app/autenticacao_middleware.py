from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AutenticacaoToken(BaseHTTPMiddleware):
    #metodo executado pra cada requisicao
    async def dispatch(self, request, call_next):
        request_path = request.url.path
        #permito que usuario sem autenticacao entrem tanto pra logar ou pra se registrar 
        if request_path.startswith("/login") or request_path.startswith("/registro"):
            return await call_next(request)
        #verifico o token
        token = request.cookies.get("session_token")
        if token != "token_senha":
            return RedirectResponse(url="/login", status_code=303)
        #retornando ao callnext se o token for igual libera o acesso
        return await call_next(request)
