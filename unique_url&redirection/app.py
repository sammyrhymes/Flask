from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the index page'

@app.route('/project/')
def project():
    return 'This is the project page'

@app.route('/about')
def about():
    return 'this is the about page'

app.run(debug=True)