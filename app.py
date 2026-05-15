from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def page():
    cursos = ["HTML", "CSS", "Javascript", "Python", "MYSQL"]
    data = {
        "titulo_tab": "Mi primera Page con Flask",
        "titulo_h1": "Bienvenid@!",
        "cursos": cursos,
        "all_cursos": len(cursos),
    }
    return render_template("index.html", data=data)

@app.route("/welcome")
def index():
    return "<h1>Bienvenido</h1>"

@app.route("/saludo/nombre/<name>")
def saludo(name):
    print(name)
    # data = {"name": name}
    return "<h1>Bienvenido</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
