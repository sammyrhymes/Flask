from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'index page'

@app.route('/user/<username>')
def user(username):
    return f'hello and welcome, {escape(username)}'

@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f'this is blog number {escape(blog_id)}'

@app.route('/path/<path:subpath>')
def path(subpath):
    return f'path to this is {escape(subpath)}'

user('sam')
blog(1)
path('/path/to/file')

app.run(debug=True)