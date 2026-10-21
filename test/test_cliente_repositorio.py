import pytest

from app.banco_de_dados.cliente_repositorio import ClienteRepositorio


class TestClienteRepositorio:

    @pytest.mark.asyncio
    async def test_listar_cliente_retorna_lista_vazia(
        self, banco_simulado
    ):
        banco, cursor = banco_simulado

        # Simula uma consulta sem clientes cadastrados
        cursor.fetchall.return_value = []

        repositorio = ClienteRepositorio(banco)

        resultado = await repositorio.listar_cliente()

        # Verifica se o resultado é uma lista vazia
        assert resultado == []

        # Verifica se a consulta SQL foi executada corretamente
        cursor.execute.assert_called_once_with(
            "SELECT id, nome, email, telefone FROM clientes"
        )


@pytest.mark.asyncio
async def test_listar_cliente_retorna_clientes(banco_simulado):
    banco, cursor = banco_simulado

    # Simula dois clientes retornados pelo banco
    cursor.fetchall.return_value = [
        (1, "João Silva", "joao@example.com", "11999999999"),
        (2, "Maria Santos", "maria@example.com", "11888888888"),
    ]

    repositorio = ClienteRepositorio(banco)

    resultado = await repositorio.listar_cliente()

    # Verifica se os dois clientes foram retornados
    assert len(resultado) == 2

    # Verifica os dados do primeiro cliente
    assert resultado[0].id_ == 1
    assert resultado[0].nome == "João Silva"
    assert resultado[0].email == "joao@example.com"

    # Verifica os dados do segundo cliente
    assert resultado[1].id_ == 2
    assert resultado[1].nome == "Maria Santos"