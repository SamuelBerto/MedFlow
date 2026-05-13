from database.conexao import conectar, criar_tabela_pacientes

conexao = conectar()

criar_tabela_pacientes()

print("🏥 MedFlow conectado ao banco com sucesso!")
print("📋 Tabela de pacientes criada com sucesso!")