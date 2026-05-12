from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Bienvenido</h1>"


@app.route("/saludo/nombre/<str:name>")
def saludo(name):
    # data = {"name": name}
    return f"<h1>Bienvenido {name}</h1>"


if __name__ == "__main__":
    app.run()
