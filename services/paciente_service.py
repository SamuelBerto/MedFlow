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

