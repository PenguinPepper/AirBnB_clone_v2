#!/usr/bin/python3
"""This module contains a script to start a flask application

This script routes a simple web server 
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    '''Function that returns text for home route'''
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
