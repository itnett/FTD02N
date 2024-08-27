python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def konfigurasjon():
    innstillinger = {
        "server_navn": "webserver1",
        "port": 80,
        "ssl_aktivert": True,
    }
    return render_template("config.html", innstillinger=innstillinger)

if __name__ == '__main__':
    app.run(debug=True)