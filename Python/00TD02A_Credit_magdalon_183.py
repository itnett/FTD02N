python
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/kjør_kommando', methods=['POST'])
def kjør_kommando():
    kommando = request.form['kommando']

    # Valider kommandoen (sjekk mot en liste over tillatte kommandoer)
    tillatte_kommandoer = ["ls", "whoami", "date"]
    if kommando not in tillatte_kommandoer:
        abort(403)  # Returner en 403 Forbidden-feil hvis kommandoen ikke er tillatt

    # Kjør kommandoen og returner resultatet
    resultat = os.popen(kommando).read()
    return resultat