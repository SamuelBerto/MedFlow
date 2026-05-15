from database.conexao import (
    criar_tabela_pacientes,
    criar_tabela_medicos
)
from utils.menu import exibir_menu

from services.paciente_service import (
    cadastrar_paciente,
    listar_pacientes,
    editar_paciente,
    deletar_paciente
)
from services.medico_service import (
    cadastrar_medico,
    listar_medicos
)
criar_tabela_pacientes()
criar_tabela_medicos()

while True:
    exibir_menu()
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        listar_pacientes()
    elif opcao == "3":
        editar_paciente()  
    elif opcao == "4":
        deletar_paciente()
    elif opcao == "5":
        cadastrar_medico()
    elif opcao == "6":
        listar_medicos()
    elif opcao == "0":
        print("👋 Encerrando o sistema...")
        break

    else:
        print("❌ Opção inválida. Por favor, escolha uma opção válida.")