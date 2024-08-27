python
from flask import Flask, Response
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import psutil
import time

app = Flask(__name__)

@app.route('/plot.png')
def plot_png():
    fig = Figure()
    ax = fig.subplots()
    cpu_bruk = []
    for i in range(10):
        cpu_bruk.append(psutil.cpu_percent())
        time.sleep(1)
    ax.plot(cpu_bruk)
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"