"""ClienteRepositorio
└── responsabilidade: GERENCIAR OS DADOS DOS USUARIOS
    ├── SELECT
    ├── INSERT
    ├── UPDATE
    └── DELETE
    """
from app.banco_de_dados.banco_local import BancoDeDadosLocal
from app.modelos.usuario import Usuario,CriarUsuario

class UsuarioRepositorio():
    def __init__(self,banco:BancoDeDadosLocal):
        self.db = banco
    async def buscar_usuarios_email_senha(self,email:str, senha:str):
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('SELECT id, nome, email FROM usuarios WHERE email=? AND senha=?',(email,senha))
            linha = cursor.fetchone()
            if linha:
                return Usuario(id=linha[0],nome=linha[1],email=linha[2])
            return None
        
    async def criar_usuarios(self,usuario:CriarUsuario):
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO usuarios (nome,email,senha) VALUES(?,?,?)',(usuario.nome,usuario.email,usuario.senha))
            id_novo = cursor.lastrowid
            return Usuario(id=id_novo,nome=usuario.nome,email=usuario.email)  
        
    async def buscar_email_usuario(self,email:str):
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id,nome,email FROM usuarios WHERE email=?",(email,))  
            linha = cursor.fetchone()
            if linha:
                return Usuario(id=linha[0], nome=linha[1],email=linha[2])
            return None
