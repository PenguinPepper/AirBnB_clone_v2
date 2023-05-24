#!/usr/bin/python3
"""
This module contains a script to start a flask application
"""


from flask import Flask
app = Flask(__name__)


@app.rout('/')
def hello_hbnb():
    '''Function that returns text for home route'''
    return 'Hello HBNB!'
