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
    