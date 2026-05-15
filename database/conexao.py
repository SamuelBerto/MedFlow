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

def criar_tabela_medicos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   especialidade TEXT NOT NULL,
                   telefone TEXT NOT NULL
                   )
                   """)
    conexao.commit()
    conexao.close()
    
def criar_tabela_consultas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   paciente_id INTEGER NOT NULL,
                   medico_id INTEGER NOT NULL,
                   data TEXT NOT NULL,
                   hora TEXT NOT NULL,
                   FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
                   FOREIGN KEY (medico_id) REFERENCES medicos(id)
                   )
                   """)
    conexao.commit()
    conexao.close()
    