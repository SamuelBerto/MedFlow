from database.conexao import (
    criar_tabela_pacientes,
    criar_tabela_medicos,
    criar_tabela_consultas
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
from services.consulta_service import (
    agendar_consulta,
    listar_consultas
)
from database.conexao import (
    criar_tabela_pacientes,
    criar_tabela_medicos,
    criar_tabela_consultas
)

criar_tabela_pacientes()
criar_tabela_medicos()
criar_tabela_consultas()
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
    elif opcao == "7":
        agendar_consulta()
    elif opcao == "8":
        listar_consultas()
    elif opcao == "0":
        print("👋 Encerrando o sistema...")
        break

    else:
        print("❌ Opção inválida. Por favor, escolha uma opção válida.")