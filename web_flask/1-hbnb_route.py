#!/usr/bin/python3
"""Module contains script that starts a flask application

Web applicatiob listesns on port 5000
"""


from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
