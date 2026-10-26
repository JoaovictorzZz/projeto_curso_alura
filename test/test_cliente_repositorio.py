
import pytest
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio, ClienteCriar, Cliente


# 1. Listar clientes com a lista vazia
@pytest.mark.asyncio
async def test_listar_cliente_retorna_lista_vazia(mock_banco_dados):
    # Arrange: preparar o banco vazio
    mock_banco_dados.cursor.fetchall.return_value = []
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: listar os clientes
    resultado = await repositorio.listar_cliente()

    # Assert: verificar o resultado e a consulta
    assert resultado == []
    mock_banco_dados.cursor.execute.assert_called_once_with(
        "SELECT id, nome, email, telefone FROM clientes"
    )


# 2. Listar clientes existentes
@pytest.mark.asyncio
async def test_listar_cliente_retorna_clientes(mock_banco_dados):
    # Arrange: simular dois clientes no banco
    mock_banco_dados.cursor.fetchall.return_value = [
        (1, "João Silva", "joao@example.com", "11999999999"),
        (2, "Maria Santos", "maria@example.com", "11888888888"),
    ]
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: listar os clientes
    resultado = await repositorio.listar_cliente()

    # Assert: verificar os clientes retornados
    assert len(resultado) == 2
    assert resultado[0].id_ == 1
    assert resultado[0].nome == "João Silva"
    assert resultado[0].email == "joao@example.com"
    assert resultado[1].id_ == 2
    assert resultado[1].nome == "Maria Santos"
    assert resultado[1].email == "maria@example.com"

    mock_banco_dados.cursor.execute.assert_called_once_with(
        "SELECT id, nome, email, telefone FROM clientes"
    )


# 3. Buscar cliente pelo ID
@pytest.mark.asyncio
async def test_obter_usuario_por_id(mock_banco_dados):
    # Arrange: simular um cliente encontrado
    mock_banco_dados.cursor.fetchone.return_value = (
        1, "Joao", "joao@email.com", "11111112"
    )
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: buscar o cliente
    resultado = await repositorio.obter_cliente(1)

    # Assert: verificar o cliente e a consulta
    assert resultado == Cliente(
        id_=1,
        nome="Joao",
        email="joao@email.com",
        telefone="11111112"
    )
    mock_banco_dados.cursor.execute.assert_called_once_with(
        "SELECT id, nome, email, telefone FROM clientes WHERE id=?",
        (1,)
    )


# 4. Criar cliente
@pytest.mark.asyncio
async def test_criar_usuario_no_banco(mock_banco_dados):
    # Arrange: preparar os dados do novo cliente
    mock_banco_dados.cursor.lastrowid = 1
    cliente = ClienteCriar(
        nome="Joao", email="jvvieira", telefone="11111112"
    )
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: criar o cliente
    resultado = await repositorio.criar_cliente(cliente)

    # Assert: verificar o cliente criado e a consulta
    assert resultado.id_ == 1
    assert resultado.nome == "Joao"
    assert resultado.email == "jvvieira"
    assert resultado.telefone == "11111112"

    mock_banco_dados.cursor.execute.assert_called_once_with(
        "INSERT INTO clientes (nome,email,telefone) VALUES(?,?,?)",
        ("Joao", "jvvieira", "11111112")
    )


# 5. Remover cliente
@pytest.mark.asyncio
async def test_remover_usuario_no_banco(mock_banco_dados):
    # Arrange: preparar o cliente que será removido
    cliente = Cliente(
        id_=1, nome="Joao", email="jvvieira", telefone="11111112"
    )
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: remover o cliente
    resultado = await repositorio.remover_cliente(cliente.id_)

    # Assert: verificar o resultado e a consulta
    assert resultado == 1
    mock_banco_dados.cursor.execute.assert_called_once_with(
        "DELETE FROM clientes WHERE id=?", (1,)
    )


# 6. Atualizar cliente
@pytest.mark.asyncio
async def test_atualizar_cliente_no_banco(mock_banco_dados):
    # Arrange: preparar os novos dados
    cliente = ClienteCriar(
        nome="Joao", email="jvvieira", telefone="11111112"
    )
    repositorio = ClienteRepositorio(mock_banco_dados)

    # Act: atualizar o cliente
    resultado = await repositorio.atualizar_cliente(
        cliente=cliente, cliente_id=1
    )

    # Assert: verificar o cliente atualizado e a consulta
    assert resultado == Cliente(
        id_=1, nome="Joao", email="jvvieira", telefone="11111112"
    )
    mock_banco_dados.cursor.execute.assert_called_once_with(
        "UPDATE FROM clientes SET nome=,email=?,telefone=? WHERE id=?",
        (cliente.nome, cliente.email, cliente.telefone, 1)
    )
