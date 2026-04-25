from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "<h1>¡Hola Mundo!</h1><p>Aplicación desplegada con CI/CD - DevOps ITLA</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

