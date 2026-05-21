from flask import Flask, render_template, request, redirect
from database.conexao import conectar

app = Flask(__name__)

@app.route("/")
def home():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM pacientes")
    total_pacientes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM medicos")
    total_medicos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM consultas")
    total_consultas = cursor.fetchone()[0]

    conexao.close()

    return render_template(
        "index.html",
        total_pacientes=total_pacientes,
        total_medicos=total_medicos,
        total_consultas=total_consultas
    )


@app.route("/pacientes")
def pacientes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM pacientes")

    pacientes = cursor.fetchall()

    lista_pacientes = []

    for paciente in pacientes:
        lista_pacientes.append({
            "id": paciente[0],
            "nome": paciente[1],
            "idade": paciente[2],
            "telefone": paciente[3],
            "genero": paciente[4]
        })

    conexao.close()

    return render_template("pacientes.html", pacientes=lista_pacientes
                           )

@app.route("/medicos")
def medicos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM medicos")

    medicos = cursor.fetchall()

    lista_medicos = []

    for medico in medicos:
        lista_medicos.append({
            "id": medico[0],
            "nome": medico[1],
            "especialidade": medico[2],
            "telefone": medico[3]
        })

    conexao.close()

    return render_template("medicos.html", medicos=lista_medicos
    )     

@app.route("/consultas")
def consultas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT
        consultas.id,
        pacientes.nome,
        medicos.nome,
        consultas.data,
        consultas.hora
    FROM consultas
    JOIN pacientes
        ON consultas.paciente_id = pacientes.id
    JOIN medicos
        ON consultas.medico_id = medicos.id
    """)

    consultas = cursor.fetchall()

    lista_consultas = []

    for consulta in consultas:
        lista_consultas.append({
            "id": consulta[0],
            "paciente": consulta[1],
            "medico": consulta[2],
            "data": consulta[3],
            "hora": consulta[4]
        })

    conexao.close()

    return render_template(
    "consultas.html",
    consultas=lista_consultas
    )


@app.route("/novo-paciente", methods=["GET", "POST"])
def novo_paciente():

    if request.method == "POST":

        nome = request.form["nome"]
        idade = request.form["idade"]
        telefone = request.form["telefone"]
        genero = request.form["genero"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO pacientes (nome, idade, telefone, genero)
            VALUES (?, ?, ?, ?)
        """, (nome, idade, telefone, genero))

        conexao.commit()
        conexao.close()

        return redirect("/pacientes")

    return render_template("novo_paciente.html")

@app.route("/editar-paciente/<int:id>", methods=["GET", "POST"])
def editar_paciente(id):
    
    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":
    
        nome = request.form["nome"]
        idade = request.form["idade"]
        telefone = request.form["telefone"]
        genero = request.form["genero"]

        cursor.execute("""
                       UPDATE pacientes
                       SET nome = ?,
                            idade = ?,
                            telefone = ?,
                            genero = ?
                          WHERE id = ?
                          """, (nome, idade, telefone, genero, id))
        conexao.commit()
        conexao.close()

        return redirect("/pacientes")
    
    cursor.execute("SELECT * FROM pacientes WHERE id = ?", (id,))

    paciente = cursor.fetchone()

    conexao.close()

    return render_template(
        "editar_paciente.html",
        paciente=paciente
    )



@app.route("/novo-medico", methods=["GET", "POST"])
def novo_medico():

    if request.method == "POST":

        nome = request.form["nome"]
        especialidade = request.form["especialidade"]
        telefone = request.form["telefone"]

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO medicos
            (nome, especialidade, telefone)
            VALUES (?, ?, ?)
        """, (nome, especialidade, telefone))

        conexao.commit()
        conexao.close()

        return redirect("/medicos")

    return render_template("novo_medico.html")

@app.route("/nova-consulta", methods = ["GET", "POST"])
def nova_consulta():

    conexao = conectar()
    cursor = conexao.cursor()

    if request.method == "POST":

        print("CONSULTA RECEBIDA")


        paciente_id = request.form ["paciente_id"]
        medico_id = request.form ["medico_id"]
        data = request.form ["data"]
        hora = request.form ["hora"]

        cursor.execute("""
            INSERT INTO consultas
            (paciente_id, medico_id, data, hora)
            VALUES (?, ?, ?, ?)
        """, (paciente_id, medico_id, data, hora))

        conexao.commit()
        conexao.close()

        return redirect("/consultas")

    cursor.execute("SELECT id, nome FROM pacientes")
    pacientes = cursor.fetchall()

    cursor.execute("SELECT id, nome, especialidade FROM medicos")
    medicos = cursor.fetchall()

    conexao.close()

    return render_template(
        "nova_consulta.html",
        pacientes=pacientes,
        medicos=medicos
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)