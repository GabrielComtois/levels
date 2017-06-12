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

@app.route('/level1/<counterLevel1>')
def level1(counterLevel1):
    return render_template("newLevel1.html", counterLevel1=counterLevel1)

@app.route('/submit', methods=['POST'])
def submit():

    return "", 201
