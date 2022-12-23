from flask import Flask, render_template, request
from .mail import sendmail
import json

app = Flask(__name__)
app.config.from_file("/etc/calat33/config.json", load=json.load)

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


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not message or not email:
            print(message, email)
            return render_template("contacto.html", notification="""
            Faltan campos email o mensaje""")

        message = f"""\
        {message}<br><br>
        <b>From:</b> {name}<br>{email}
        """

        subject = "Contacto Web"

        sendmail(message, subject, [email])

        return render_template("apology.html", notification="Mensaje Enviado!")

    return render_template("contacto.html")
