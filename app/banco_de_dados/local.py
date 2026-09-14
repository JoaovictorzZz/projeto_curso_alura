"""BancoDeDadosLocal
└── responsabilidade: GERENCIAR A CONEXÃO
    ├── abrir
    ├── commit
    ├── rollback
    └── fechar

"""
import sqlite3
#
from contextlib import contextmanager
#implementlando nosso banco de dados
class BancoDeDadosLocal():
    def __init__(self,nome_arquivo = "techlog.db"):
        self.nome_arquivo = nome_arquivo
        self.inicializar_banco()
    #controlando o contexto pra lidar com a infraestrutura do banco e as rotas do FASTAPI so usa o banco
    @contextmanager
    def conectar(self):
        # ABRE A CONEXAO 
        conexao = sqlite3.connect(self.nome_arquivo)
        try:
            #ENTREGA E PAUSA
            yield conexao
            #VOLTA AQUI depois do with 
            conexao.commit()
        except Exception as e:
            # Se deu erro desfaz
            conexao.rollback()
        finally:
            # Sempre fecha
            conexao.close()
        #
    def inicializar_banco(self):
            with self.conectar() as conexao:
                cursor = conexao.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cliente (
                        id INTENGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telefone TEXT NOT NULL
                    )
                ''') 
                
        
