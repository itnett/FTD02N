python
from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/status')
def system_status():
    cpu_bruk = psutil.cpu_percent()
    minne_bruk = psutil.virtual_memory().percent
    return render_template("status.html", cpu_bruk=cpu_bruk, minne_bruk=minne_bruk)