from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/about')
def about():
    return 'about page'

@app.route('/blog')
def blog():
    return 'blog page'

@app.route('/contacts')
def contact():
    return 'contact page'

app.run(debug=True)