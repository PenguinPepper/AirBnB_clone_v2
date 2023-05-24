#!/usr/bin/python3
"""This module contains a script to start a flask application

This script routes a simple web server 
"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.rout('/')
def hello_hbnb():
    '''Function that returns text for home route'''
    return 'Hello HBNB!'
