from database.conexao import conectar


def agendar_consulta():
    conexao = conectar()
    cursor = conexao.cursor()

    paciente_id = input("ID do paciente: ")
    medico_id = input("ID do médico: ")
    data = input("Data da consulta (DD/MM/AAAA): ")
    horario = input("Horário da consulta: ")

    cursor.execute("""
    INSERT INTO consultas (
        paciente_id,
        medico_id,
        data,
        horario
    )
    VALUES (?, ?, ?, ?)
    """, (paciente_id, medico_id, data, horario))

    conexao.commit()
    conexao.close()

    print("📅 Consulta agendada com sucesso!")


def listar_consultas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        consultas.id,
        pacientes.nome,
        medicos.nome,
        consultas.data,
        consultas.horario
    FROM consultas
    JOIN pacientes
        ON consultas.paciente_id = pacientes.id
    JOIN medicos
        ON consultas.medico_id = medicos.id
    """)

    consultas = cursor.fetchall()

    print("\n📅 LISTA DE CONSULTAS\n")

    for consulta in consultas:
        print(f"""
ID Consulta: {consulta[0]}
Paciente: {consulta[1]}
Médico: {consulta[2]}
Data: {consulta[3]}
Horário: {consulta[4]}
-------------------------
""")

    conexao.close()