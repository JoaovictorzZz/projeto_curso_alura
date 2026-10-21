from contextlib import nullcontext
from unittest.mock import MagicMock
import pytest
#Apenas construímos o ambiente que permitirá executar o teste.
@pytest.fixture
def banco_simulado():
    banco = MagicMock()
    conexao = MagicMock()
    cursor = MagicMock()
    #
    banco.conectar.return_value = nullcontext(conexao)
    conexao.cursor.return_value = cursor

    return banco,cursor