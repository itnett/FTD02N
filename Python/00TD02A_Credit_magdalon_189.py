python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/logger')
def logger():
    loggoppføringer = [
        {"tidspunkt": "2023-06-13 10:22:31", "nivå": "INFO", "melding": "Bruker logget inn"},
        {"tidspunkt": "2023-06-13 10:25:14", "nivå": "ADVARSEL", "melding": "Ugyldig innloggingsforsøk"},
        {"tidspunkt": "2023-06-13 10:30:05", "nivå": "FEIL", "melding": "Serverfeil"},
    ]
    return render_template("logger.html", loggoppføringer=loggoppføringer)