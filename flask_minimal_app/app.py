from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return '<p>Hello world</p>'

app.run(debug=True)