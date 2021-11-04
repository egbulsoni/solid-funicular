from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='Eduardo'):
    return render_template('user.html', nombre=name)

if __name__ == '__main__':
    app.run(debug = True, port = 8080)