from flask import Flask, request, session

app = Flask(__name__)
app.secret_key = 'some_secret_key'


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/hello')
def hello():
    name = request.args.get('name')
    return f'Hello, {name, request.__dict__}!'


@app.route('/set_session')
def set_session():
    session['username'] = 'John'
    return 'Session value set'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username:
        return 'Hello, {}'.format(username)
    else:
        return 'No session value set'
    

if __name__ == '__main__':
    app.run(debug=True)
    