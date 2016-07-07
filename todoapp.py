from flask import Flask, render_template
from api import api_bp
import argparse
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(api_bp)


@app.route('/')
def index():
    return render_template('index.html')


