from database.conexao import conectar

def cadastrar_medico():
    conexao = conectar()
    cursor = conexao.cursor()

    nome = input("Nome do médico: ").strip()

    if nome == "":
        print("❌ O nome não pode ficar vazio!")
        return
    especialidade = input("Especialidade do médico: ").strip()

    if especialidade == "":
        print("❌ A especialidade não pode ficar vazia!")
        return
    telefone = input("Telefone do médico: ").strip()

    if telefone == "":
        print("❌ O telefone não pode ficar vazio!")
        return
    
    cursor.execute ("""
                    INSERT INTO medicos (nome, especialidade, telefone) VALUES (?, ?, ?)
                    """, (nome, especialidade, telefone))
    conexao.commit()
    conexao.close()

    print("✅ Médico cadastrado com sucesso!")

    def listar_medicos():
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM medicos")

        medicos = cursor.fetchall()

        print("\n 👨‍⚕️ Lista de Médicos:\n")
        for medico in medicos:
            print(f"""
                  ID: {medico[0]}
                  Nome: {medico[1]}
                  Especialidade: {medico[2]}
                  Telefone: {medico[3]}
                  -------------------------
                  """)
        conexao.close()
        