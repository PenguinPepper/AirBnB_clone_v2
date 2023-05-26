#!/usr/bin/python3
"""Module contains script that starts a flask application

Web application listesns on port 5000
"""


from flask import Flask, escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    ''''Returns text for home route'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Return hbnb text'''
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    '''Return a special message for C'''
    return 'C {}'.format(escape(text.replace("_", " ")))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    '''Return a special message for Python'''
    return 'Python {}'.format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
