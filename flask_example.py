from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/hello')
def hello():
    name = request.args.get('name')
    return f'Hello, {name, request.__dict__}!'

if __name__ == '__main__':
    app.run(debug=True)
    