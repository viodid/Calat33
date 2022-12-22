from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/artista")
def route():
    return render_template("artista.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/colaboraciones")
def colaboraciones():
    return render_template("colaboraciones.html")
