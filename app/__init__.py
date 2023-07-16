from flask import Flask, render_template, request
from redmail import gmail
import json
import os

app = Flask(__name__)

#with open('/etc/calat33/config.json') as config_file:
#    config = json.load(config_file)

gmail.username = os.environ["EMAIL_SENDER"]
gmail.password = os.environ["EMAIL_PASSWORD"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/artista")
def route():
    return render_template("artista.html")


@app.route("/galeria")
def galeria():
    return render_template("galeria.html")


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
            return render_template("contacto.html", notification="""
            Faltan campos email o mensaje""")

        message = f"""\
        {message}<br><br>
        <b>From:</b> {name}<br>{email}
        """

        subject = "Contacto Web"

        sendmail(message, subject, [os.environ["EMAIL_SENDER"]])

        return render_template("contacto.html", notification="Mensaje enviado, pronto recibirás una respuesta!")

    return render_template("contacto.html")


def sendmail(message_client, subject, recipients):
    message = f"""\
        <html>
            <body style="padding:1.5rem; background: transparent;
            font-size:1.1rem; font">
                <div style="display:flex; justify-content:center; align-items:
                center; margin-bottom:2rem;">
                    <!--
                    <img src="https://i.ibb.co/xmtSkh6/calat-email.png" style="max-width:300px">
                    -->
                    <img src="https://i.ibb.co/3TYTkDd/New-calart-solecito.png" style="max-width:300px">
                </div>
                <p>{message_client}</p>
                <div>
                    <a href="https://www.facebook.com/CALAT-33-169199418110806" style='margin-right: 0.5rem;'>
                        Facebook
                    </a>
                    <a href="https://www.instagram.com/calat33/" style='margin-right: 0.5rem;'>
                        Instagram
                    </a>
                    <a href="https://twitter.com/hashtag/calat33">
                        Twitter
                    </a>
                </div>
            </body>
        </html>
        """
    gmail.send(
        subject=subject,
        receivers=recipients,
        html=message
    )
    return True
