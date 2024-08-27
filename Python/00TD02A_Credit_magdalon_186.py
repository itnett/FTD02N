python
from flask import Flask, render_template, request
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# ... (modellfunksjon og tegne_linreg-funksjon som i blogginnlegget)

@app.route('/linreg', methods=['GET', 'POST'])
def show_linreg():
    if request.method == 'POST':
        x_data = [float(x) for x in request.form.getlist('x') if x]
        y_data = [float(y) for y in request.form.getlist('y') if y]
        inndata = f"x: {x_data}<br>y: {y_data}"

        if len(x_data) != len(y_data) or len(x_data) < 2:
            utdata = "Ugyldig input. Du må ha minst to datapunkter, og like mange x- og y-verdier."
        else:
            løsning = linreg(x_data, y_data)
            utdata = f"<p>Regresjonslinje: y = {løsning['a']:.3g}x + {løsning['b']:.3g}</p>\n"
            utdata += tegn_linreg(løsning['funksjon'], x_data, y_data)

    else:
        inndata = ""
        utdata = ""

    return render_template("linreg.html", skjema=skjema, inndata=inndata, utdata=utdata)