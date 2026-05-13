import sqlite3

def conectar():
    conexao = sqlite3.connect('medflow.db')
    return conexao
