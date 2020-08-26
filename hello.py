from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Test</h1>'

@app.route('/user/<name>')
def greet(name):
    return f'Hello {name}'
