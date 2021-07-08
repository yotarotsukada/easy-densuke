# coding: utf-8

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', title='login')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        if name == '':
            name = 'guest user'
        name = ', ' + name
    if request.method == 'GET':
            name = ''
    return render_template('hello.html', title='hello', name=name) 

@app.route('/result', methods=['POST'])
def judge():
    try:
        number = int(request.form['number'])
    except ValueError:
        return render_template('error.html', title='error')
    if (number % 3 == 0) or ('3' in str(number)):
        result = '(*＾∀ﾟ) NABE-ATSU!!'
    else:
        result = '(-_-) nah'
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)