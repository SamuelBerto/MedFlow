from database.conexao import criar_tabela_pacientes
from services.paciente_service import (
    cadastrar_paciente,
    listar_pacientes,
    editar_paciente,
    deletar_paciente
)

criar_tabela_pacientes()

while True:
    print("\n🏥 MEDFLOW")
    print("Bem-vindo ao sistema de gerenciamento de pacientes!")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Editar paciente")
    print("4. Deletar paciente")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        listar_pacientes()
    elif opcao == "3":
        editar_paciente()  
    elif opcao == "4":
        deletar_paciente()
    elif opcao == "0":
        print("👋 Encerrando o sistema...")
        break

    else:
        print("❌ Opção inválida. Por favor, escolha uma opção válida.")