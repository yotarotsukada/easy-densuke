# coding: utf-8

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    hello = 'hello world'
    return hello
 
if __name__ == '__main__':
    app.run()