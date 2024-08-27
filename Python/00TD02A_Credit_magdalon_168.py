python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hei_verden():
    return "Hei, verden fra Flask!"

if __name__ == '__main__':
    app.run(debug=True)