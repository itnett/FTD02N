python
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/kommando/<kommando>')
def kjør_kommando(kommando):
    # Sjekk om kommandoen er tillatt
    tillatte_kommandoer = ["ls", "whoami", "date"]
    if kommando not in tillatte_kommandoer:
        abort(403)  # Returner en 403 Forbidden-feil hvis kommandoen ikke er tillatt

    # Kjør kommandoen og returner resultatet
    resultat = os.popen(kommando).read()
    return resultat