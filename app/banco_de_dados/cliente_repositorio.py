"""ClienteRepositorio
└── responsabilidade: GERENCIAR OS DADOS DOS CLIENTES
    ├── SELECT
    ├── INSERT
    ├── UPDATE
    └── DELETE
    """
#gerenciar conexão com o banco , so que com as querys do cliente

from app.banco_de_dados.banco_local import BancoDeDadosLocal
from app.modelos.cliente import Cliente

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