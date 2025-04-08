import sqlite3 # é uma biblioteca de banco de dados leve e embutida que implementa um sistema de 
                # gerenciamento de banco de dados relacional (RDBMS) 

def criar_banco():
    """
    Cria ou abre o arquivo usuarios.db,
    cria a tabela se não existir e retorna
    (conexao, cursor).
    """
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            email TEXT PRIMARY KEY,
            hash_senha TEXT NOT NULL
        )
    ''')
    conexao.commit()
    return conexao, cursor

def fechar_banco(conexao):
    """
    Fecha a conexão com o banco.
    """
    conexao.close()