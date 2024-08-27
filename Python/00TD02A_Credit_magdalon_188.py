python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hilsen/<navn>')
def hilsen(navn):
    alder = 30
    return render_template("hilsen.html", navn=navn, alder=alder)