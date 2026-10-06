"""BancoDeDadosLocal
└── responsabilidade: GERENCIAR A CONEXÃO
    ├── abrir
    ├── commit
    ├── rollback
    └── fechar
└── criar padrao da tabela no banco


"""
import sqlite3
#
from contextlib import contextmanager
#implementlando nosso banco de dados
class BancoDeDadosLocal():
    def __init__(self,nome_arquivo = "techlog.db"):
        self.nome_arquivo = nome_arquivo
    #controlando o contexto pra lidar com a infraestrutura do banco. - as rotas do FASTAPI so usa o banco sem se preocupar 
    @contextmanager
    def conectar(self):
        conexao = sqlite3.connect(self.nome_arquivo)
        #ABRE
        try:
             yield conexao
             #salva
             conexao.commit()
        except Exception as e:
             #se der erro desfaz
             conexao.rollback()
             raise e 
        finally:
             #fechando a conexão
             conexao.close()
    #aqui eu so tenho o trabalho de chamar a conexao do banco e ja sair metendo comandos SQL no caso aqui criar a tabela
    def inicializar_banco(self):
            with self.conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS clientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT NOT NULL
                    )
                ''') 
                
        
