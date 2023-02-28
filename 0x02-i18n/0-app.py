#!/usr/bin/env python3
"""This script starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """This function executes when the 0.0.0.0:5000/ is requested"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
