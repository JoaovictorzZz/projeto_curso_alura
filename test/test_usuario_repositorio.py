import pytest
from pwdlib import PasswordHash

from app.banco_de_dados.usuario_repositorio import UsuarioRepositorio
from app.modelos.usuario import CriarUsuario


password_hash = PasswordHash.recommended()


@pytest.mark.asyncio
async def test_criar_usuario_salva_hash_da_senha(mock_banco_dados):
    mock_banco_dados.cursor.lastrowid = 1
    repositorio = UsuarioRepositorio(mock_banco_dados)
    usuario = CriarUsuario(
        nome="Joao",
        email="joao@example.com",
        senha="senha-segura",
    )

    resultado = await repositorio.criar_usuarios(usuario)

    valores_salvos = mock_banco_dados.cursor.execute.call_args.args[1]
    senha_salva = valores_salvos[2]
    assert resultado.id == 1
    assert senha_salva != usuario.senha
    assert password_hash.verify(usuario.senha, senha_salva)


@pytest.mark.asyncio
async def test_login_compara_senha_com_hash_salvo(mock_banco_dados):
    senha_hash = password_hash.hash("senha-segura")
    mock_banco_dados.cursor.fetchone.return_value = (
        1,
        "Joao",
        "joao@example.com",
        senha_hash,
    )
    repositorio = UsuarioRepositorio(mock_banco_dados)

    resultado = await repositorio.buscar_usuarios_email_senha(
        "joao@example.com",
        "senha-segura",
    )

    assert resultado.id == 1
    mock_banco_dados.cursor.execute.assert_called_once_with(
        "SELECT id, nome, email, senha FROM usuarios WHERE email=?",
        ("joao@example.com",),
    )


@pytest.mark.asyncio
async def test_login_rejeita_senha_incorreta(mock_banco_dados):
    mock_banco_dados.cursor.fetchone.return_value = (
        1,
        "Joao",
        "joao@example.com",
        password_hash.hash("senha-segura"),
    )
    repositorio = UsuarioRepositorio(mock_banco_dados)

    resultado = await repositorio.buscar_usuarios_email_senha(
        "joao@example.com",
        "senha-incorreta",
    )

    assert resultado is None


@pytest.mark.asyncio
async def test_login_rejeita_senha_armazenada_em_texto_puro(mock_banco_dados):
    mock_banco_dados.cursor.fetchone.return_value = (
        1,
        "Joao",
        "joao@example.com",
        "senha-segura",
    )
    repositorio = UsuarioRepositorio(mock_banco_dados)

    resultado = await repositorio.buscar_usuarios_email_senha(
        "joao@example.com",
        "senha-segura",
    )

    assert resultado is None
