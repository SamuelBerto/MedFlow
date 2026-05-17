from flask import Flask
from database.conexao import conectar

app = Flask(__name__)


@app.route("/")
def home():
    return "🏥 MedFlow API Online!"


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

    return lista_pacientes

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

    return lista_medicos


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)