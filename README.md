# Instalar aplicação
pip install -r requirements.txt

# Instalar ambiente de desenvolvimento e testes
pip install -r requirements-dev.txt

# Rodando aplicação com Docker
docker run --rm -p 8000:8000 techlog:v1

# Techlog Solutions - CRM
A empresa Techlog Solutions nos contratou para criar um website para cadastrar seus clientes e suas ordens de serviço. Para isso, vamos utilizar Python junto com FastAPI, desenvolvendo tanto o backend quanto o frontend

## Pré Requisitos:

- Python Básico
- Métodos HTTPs
- HTML, CSS, JS Básicos
- Orientação a Objetos em Python

## Ferramentas:

- Python
- FastAPI
- Jinja
- Uvicorn
- Sqlite
- Pytests

## Senhas de usuários

As senhas são armazenadas como hashes Argon2 usando `pwdlib`; a aplicação não
precisa nem deve descriptografar ou exibir a senha original. No cadastro, o
repositório gera o hash antes de gravar o usuário. No login, ele busca o hash
pelo e-mail e verifica a senha enviada com `PasswordHash.verify`.

