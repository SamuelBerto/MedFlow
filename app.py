from flask import Flask

app = Flask(__name__)


@app.route("/pacientes")
def pacientes():
    return "🏥 Lista de Pacientes"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)