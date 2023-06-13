#!/usr/bin/python3
"""Module contains script that starts a flask application

Web application listesns on port 5000
"""


from flask import Flask, escape, render_template
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


@app.route('/number/<int:n>')
def number(n):
    '''Return n if it is an integer'''
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    '''Renders a HTML with thw number'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''Renders an HTML page only if n is an integer'''
    # return 'The issue is in the html page'
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
