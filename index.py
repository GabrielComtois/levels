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
maxNumberOfLevelsID = 10
maxNumberOfKeywords = 15

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/level1/<counterLevel1>')
def level1(counterLevel1):
    return render_template("newLevel1.html", counterLevel1=counterLevel1)

@app.route('/level2/<counterLevel2>')
def level2(counterLevel2):
    return render_template("newLevel2.html", counterLevel2=counterLevel2)

@app.route('/submit', methods=['POST'])
def submit():
    jsonData = []
    for x in range(1, maxNumberOfLevelsID):
        data = {}
        level1name = request.form.get(str(x) + 'Level1Nom', None)

        tablevel1keyword = []
        level1keyword = request.form.get(str(x) + 'Level1Keyword', None)
        if level1keyword:
            tablevel1keyword = level1keyword.split(',')

        level1action = request.form.get(str(x) + 'Level1Action', None)

        if level1name and tablevel1keyword: # if level1, keyword entered
            if level1action: # avec action
                print level1name + level1action
                print tablevel1keyword
                data[str(x) + 'Level1Name'] = level1name# premier objet json
                data[str(x) + 'level1Action'] = level1action
                data[str(x) + 'Level1Keywords'] = json.dumps(tablevel1keyword)
                jsonData.append(data)
            else: # sans action (level 2)

                print "sans action"
    finalJson = json.dumps(jsonData)
    return finalJson, 201
