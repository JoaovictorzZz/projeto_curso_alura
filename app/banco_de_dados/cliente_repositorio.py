"""ClienteRepositorio
└── responsabilidade: GERENCIAR OS DADOS DOS CLIENTES
    ├── SELECT
    ├── INSERT
    ├── UPDATE
    └── DELETE
    """
#gerenciar conexão com o banco , so que com as querys do cliente

from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelos.cliente import Cliente

class ClienteRepositorio:
    def __init__(self, banco_de_dados:BancoDeDadosLocal):
        self.db = banco_de_dados
    #listando os clientes
    def listar_cliente(self) -> list[Cliente]:
        with self.db.conectar() as conexao:
            cursor = conexao.cursor() # obj que le e executa comandos no banco 
            cursor.execute('SELECT id, nome, email, telefone FROM clientes') # passando o comandos SQL
            linhas = cursor.fetchall() # pegando todas a linhas do tabela 
            clientes =  [
                Cliente(id_=linha[0], nome=linha[1], email=linha[2], telefone=linha[3])
                for linha in linhas
            ]
            return clientes