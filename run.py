from flask import Flask
from flask import request

app = Flask(__name__)#nuevo objeto,

@app.route('/')
def index():
    return 'Cambio.'


@app.route('/params')
def saluda():
    return 'Otro mensaje.'

if __name__ == '__main__':
    app.run(debug = False, port= 8000)