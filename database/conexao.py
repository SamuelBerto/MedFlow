import sqlite3

def conectar():
    conexao = sqlite3.connect('medflow.db')
    return conexao

def criar_tabela_pacientes():
    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER,
                   telefone TEXT,
                   genero TEXT
                   )
                   """)
    conexao.commit()
    conexao.close()
