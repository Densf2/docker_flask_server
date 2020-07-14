from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(userame):
    return '{}\'s profile'.format(escape(userame))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
