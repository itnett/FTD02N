python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/behandle_data', methods=['POST'])
def behandle_data():
    brukernavn = request.form['brukernavn']
    passord = request.form['passord']
    # Valider og prosesser brukernavn og passord
    # ...
    return "Innlogging vellykket!"