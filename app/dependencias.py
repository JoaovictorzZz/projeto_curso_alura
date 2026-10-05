#Depends
from fastapi import Depends
from typing import Annotated 
#
from app.banco_de_dados.banco_local import BancoDeDadosLocal
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio

banco_de_dados = BancoDeDadosLocal()

def obter_banco() -> BancoDeDadosLocal:
    return banco_de_dados
#banco_de_dados_local é um BancoDeDadosLocal, e o FastAPI deve obtê-lo chamando obter_banco().
def obter_cliente_repositorio() -> ClienteRepositorio:
    return ClienteRepositorio(banco_de_dados)

RepoCliente = Annotated[ClienteRepositorio,Depends(obter_cliente_repositorio)]
   