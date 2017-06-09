# coding: utf8
# index.py

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import Response
from flask import jsonify
import re
import json

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('form.html')
