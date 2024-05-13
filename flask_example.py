from flask import Flask, request, session, render_template, redirect
import jinja2


app = Flask(__name__)
app.secret_key = 'some_secret_key'
loader = jinja2.FileSystemLoader('templates')


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


# модель
def get_data_from_database():
    data = {
        'name': 'Вася',
        'verb': 'like',
    }
    return data


# представление
@app.route('/start')
def start():
    name = request.args.get('name')
    verb = request.args.get('verb')
    data = get_data_from_database()
    if name:
        data['name'] = name
    if verb:
        data['verb'] = verb
    return render_template('index.html', data=data)


# контроллер
@app.route('/submit', methods=['POST'])
def submit():
    # код для обработки данных, полученных из формы
    name = request.form['name']
    verb = request.form['verb']
    # сохранение данных в базу данных
    return redirect(f'/start?name={name}&verb={verb}')


if __name__ == '__main__':
    app.run(debug=True)
    