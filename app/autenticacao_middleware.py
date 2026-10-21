from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

class AutenticacaoToken(BaseHTTPMiddleware):
    #metodo executado pra cada requisicao
    async def dispatch(self, request, call_next):
        response_path = request.url.path
        #
        if response_path.startswith("/login") or response_path.startswith("/registro"):
            return await call_next(request)
        #token e validação
        token = request.cookies.get("session_token")
        if token != "token_senha":
            return RedirectResponse(url="/login",status_code=303)
        #retorno o callnext se proseguir 
        return await call_next(request)
        
