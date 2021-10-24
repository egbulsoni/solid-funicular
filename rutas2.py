from flask import Flask
from flask import request

app = Flask(__name__)#nuevo objeto,

@app.route('/')
def index():
    return 'Hola mundo.'

# http://localhost:8000/params?params1=Eduardo_Ismael&params2=test_dos

#params/libros/ismael
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'este es un valor por default', num = 'nada'):
    return 'El parametro es {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)