# coding: utf-8

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', title='login')


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form['name']
    return render_template('hello.html', title='hello', name=name) 

@app.route('/judge', methods=['POST'])
def judge():
    number = int(request.form['number'])
    if (number % 3 == 0) or ('3' in str(number)):
        res = '(*＾∀ﾟ)'
    else:
        res = '(-_-)'
    return render_template('nabeatsu.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)