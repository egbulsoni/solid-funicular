from flask import Flask
from flask import request

app = Flask(__name__)#nuevo objeto,

@app.route('/')
def index():
    return 'Hola mundo.'

# http://localhost:8000/params?params1=Eduardo_Ismael&params2=test_dos

@app.route('/params')
def params():
    param = request.args.get('params1', 'no contiene este parametro')
    param_dos = request.args.get('params2', 'no contiene este parametro')
    return 'Los parametros son es {} {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)