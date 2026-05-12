from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"

@app.route("/saludo/nombre/<name>")
def saludo(saludo):
    return "<h1>Bienvenido {saludo}</h1>"

if __name__ == "__main__":
    app.run()