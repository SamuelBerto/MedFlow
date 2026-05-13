from database.conexao import  criar_tabela_pacientes
from services.paciente_service import cadastrar_paciente

criar_tabela_pacientes()

print("🏥 MEDFLOW")
print("Bem-vindo ao sistema de gerenciamento de pacientes!")
print("1. Cadastrar paciente")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    cadastrar_paciente()
