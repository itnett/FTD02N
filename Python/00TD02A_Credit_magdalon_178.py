python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/søk', methods=['GET', 'POST'])
def søk_i_logg():
    if request.method == 'POST':
        søkeord = request.form['søkeord']
        # Utfør søk i loggfilen basert på søkeord
        resultater = ...
        return render_template("resultater.html", resultater=resultater)
    else:
        return render_template("søk.html")