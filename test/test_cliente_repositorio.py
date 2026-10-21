import pytest

from app.banco_de_dados.cliente_repositorio import ClienteRepositorio


class TestClienteRepositorio:

    @pytest.mark.asyncio
    async def test_listar_cliente_retorna_lista_vazia(
        self, banco_simulado
    ):
        banco, cursor = banco_simulado

        cursor.fetchall.return_value = []

        repositorio = ClienteRepositorio(banco)

        resultado = await repositorio.listar_cliente()
    #vereficando com assert 
        assert resultado == []

        cursor.execute.assert_called_once_with(
            "SELECT id, nome, email, telefone FROM clientes"
        )

@pytest.mark.asyncio
async def test_listar_cliente_retorna_clientes(
     banco_simulado
):
    banco, cursor = banco_simulado

    cursor.fetchall.return_value = [
        (1, "João Silva", "joao@example.com", "11999999999"),
        (2, "Maria Santos", "maria@example.com", "11888888888"),
    ]

    repositorio = ClienteRepositorio(banco)

    resultado = await repositorio.listar_cliente()

    assert len(resultado) == 2

    assert resultado[0].id_ == 1
    assert resultado[0].nome == "João Silva"
    assert resultado[0].email == "joao@example.com"

    assert resultado[1].id_ == 2
    assert resultado[1].nome == "Maria Santos"