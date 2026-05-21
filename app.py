from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.before_request
def before_request():
    print("Antes de las peticiones")


@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response


@app.route("/")
def page():
    cursos = ["HTML", "CSS", "Javascript", "Python", "MYSQL"]
    data = {
        "head": {
            "title_tab": "Mi primera Page con Flask",
        },
        "titulo_h1": "Bienvenid@!",
        "cursos": cursos,
        "all_cursos": len(cursos),
    }
    return render_template("index.html", data=data)


@app.route("/landing-flask")
def ladingFlask():
    data = {
        "head": {
            "title_tab": "Flask",
        }
    }
    return render_template("landingFlask.html", data=data)


# @app.route("/calculator")
# def calculator():
#     data = {
#         "head": {
#             "title_tab": "Flask",
#         }
#     }
#     return render_template("calculator.html")


@app.route("/welcome")
def index():
    return "<h1>Bienvenido</h1>"


@app.route("/saludo/nombre/<name>")
def saludo(name):
    print(name)
    # data = {"name": name}
    return "<h1>Bienvenido</h1>"


@app.route("/aprendizaje/<name>/<int:age>")
def aprendizaje(name, age):
    data = {
        "head": {
            "title_tab": "Apredizaje",
        },
        "name": name,
        "age": age,
    }
    # query params :3
    print(request.args)
    print(request.args.get("sort"))
    return render_template("./aprendizaje/aprendizaje.html", data=data)


def not_found_page(error):
    return render_template("404.html"), 404


@app.route("/redireccionador")
def redirect_page_index():
    return redirect(url_for("index"))


if __name__ == "__main__":
    # app.add_url_rule('/route', view_func= name)
    app.register_error_handler(404, not_found_page)
    app.run(debug=True, port=5000)
