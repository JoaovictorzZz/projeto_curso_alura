"""ClienteRepositorio
└── responsabilidade: GERENCIAR OS DADOS DOS CLIENTES
    ├── SELECT
    ├── INSERT
    ├── UPDATE
    └── DELETE
    """
#gerenc
# iar conexão com o banco , so que com as querys do cliente

from app.banco_de_dados.banco_local import BancoDeDadosLocal
from app.modelos.cliente import Cliente,ClienteCriar

class ClienteRepositorio:
    def __init__(self, banco_de_dados:BancoDeDadosLocal):
        self.db = banco_de_dados
    #listando os clientes
    async def listar_cliente(self) -> list[Cliente]:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor() # obj que le e executa comandos no banco 
            cursor.execute('SELECT id, nome, email, telefone FROM clientes') # passando o comandos SQL
            linhas = cursor.fetchall() # pegando todas a linhas do tabela 
            clientes =  [
                Cliente(id_=linha[0], nome=linha[1], email=linha[2], telefone=linha[3])
                for linha in linhas
            ]
        return clientes
    #obter cliente por ID
    async def obter_cliente(self, cliente_id: int) -> Cliente | None:
        #primeiro preciso de uma conexão com o banco entao:
        with self.db.conectar() as conexao:
            #conectando o cursor com o banco pra poder executar comandos SQL
            cursor = conexao.cursor()
            cursor.execute(
                'SELECT id, nome, email, telefone FROM clientes WHERE id=?',(cliente_id,)
            )
            linha = cursor.fetchone()#pegando somente a primeira linha
            if linha:
                return Cliente(id_=linha[0], nome=linha[1], email=linha[2], telefone=linha[3])
            else:
                return None
    #criar cliente
    async def criar_cliente(self, cliente:ClienteCriar) -> Cliente:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO clientes (nome,email,telefone) VALUES(?,?,?)',(cliente.nome,cliente.email,cliente.telefone))
            novo_id = cursor.lastrowid
            return Cliente(id_=novo_id,nome=cliente.nome,email=cliente.email,telefone=cliente.telefone)
        return {'Cliente cadastrado com sucesso'}
        
    #remover cliente
    async def remove_cliente(self,cliente_id:int) -> Cliente | None:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM clientes WHERE id=?',(cliente_id,))
        return {f"Usuario {cliente_id} removido com sucesso"}
    #atualizar cliente
    async def atualizar_cliente(self,cliente_id:int,cliente:ClienteCriar) -> Cliente | None:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute('UPDATE clientes SET nome =?, email =? , telefone = ? WHERE id=?',(cliente.nome,cliente.email,cliente.telefone,cliente_id))
            return Cliente(id_=cliente_id,nome=cliente.nome,email=cliente.email,telefone=cliente.telefone)
            