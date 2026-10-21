from contextlib import nullcontext
from unittest.mock import MagicMock
import pytest


# Prepara os objetos simulados para os testes
@pytest.fixture
def banco_simulado():
    banco = MagicMock()
    conexao = MagicMock()
    cursor = MagicMock()

    # Simula a conexão com o banco de dados
    banco.conectar.return_value = nullcontext(conexao)

    # Simula o cursor que executa comandos SQL
    conexao.cursor.return_value = cursor

    # Disponibiliza os objetos para o teste
    return banco, cursor