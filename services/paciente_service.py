from database.conexao import conectar

def cadastrar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))
    telefone = input("Telefone do paciente: ")
    genero = input("Gênero do paciente: ")

    cursor.execute("INSERT INTO pacientes (nome, idade, telefone, genero) VALUES (?, ?, ?, ?)", (nome, idade, telefone, genero))

    conexao.commit()
    conexao.close()

    print("✅ Paciente cadastrado com sucesso!")

def listar_pacientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT *FROM pacientes")

    pacientes = cursor.fetchall()

    print("\n📋 Lista de Pacientes:\n")
    
    for paciente in pacientes:
        print(f"""
              ID: {paciente[0]}
              Nome: {paciente[1]}
              Idade: {paciente[2]}
              Telefone: {paciente[3]}
              Gênero: {paciente[4]}
              -------------------------
              """)
    conexao.close()

def editar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()

    id_paciente = input("Digite o ID do paciente: ")

    novo_nome = input("Novo nome do paciente: ")
    nova_idade = input("Nova idade do paciente: ")
    novo_telefone = input("Novo telefone do paciente: ")
    novo_genero = input("Novo gênero do paciente: ")

    cursor.execute("""UPDATE pacientes
                    SET nome = ?, idade = ?, telefone = ?, genero = ?
                    WHERE id = ?""", (novo_nome, nova_idade, novo_telefone, novo_genero, id_paciente))
    conexao.commit()
    conexao.close()

    print("✅ Paciente atualizado com sucesso!")

def deletar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()

    id_paciente = input("Digite o ID do paciente a ser deletado: ")

    cursor.execute("""DELETE FROM pacientes WHERE id = ?""", (id_paciente,))

    conexao.commit()
    conexao.close()

    print("🗑️ Paciente deletado com sucesso!✅")