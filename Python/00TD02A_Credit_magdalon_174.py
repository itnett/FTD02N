python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sikkerhetsoversikt():
    hendelser = [
        {"tidspunkt": "2023-06-13 10:25:14", "type": "Ugyldig innlogging", "ip_adresse": "192.168.1.100"},
        {"tidspunkt": "2023-06-12 15:38:02", "type": "Port scanning", "ip_adresse": "192.168.1.200"},
    ]
    return render_template("sikkerhet.html", hendelser=hendelser)