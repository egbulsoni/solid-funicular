from flask import Flask
from flask import render_template

app = Flask(__name__)#nuevo objeto,

# http://localhost:8000/params?params1=Eduardo_Ismael&params2=test_dos



@app.route('/user/<name>')
def params(name = 'Eduardo'):
    age = 17
    mylist = [1,2,3,4,5,6,7,8,9,10]
    return render_template('user.html', name = name, age= age, list = mylist)

if __name__ == '__main__':
    app.run(debug = True, port= 8000)