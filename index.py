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
maxNumberOfLevelsID = 20

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/level1/<counterLevel1>')
def level1(counterLevel1):
    return render_template("newLevel1.html", counterLevel1=counterLevel1)

@app.route('/level2/<counterLevel1>/<counterLevel2>')
def level2(counterLevel1, counterLevel2):
    return render_template("newLevel2.html", counterLevel1=counterLevel1, counterLevel2=counterLevel2)

@app.route('/level3/<counterLevel1>/<counterLevel2>/<counterLevel3>')
def level3(counterLevel1, counterLevel2, counterLevel3):
    return render_template("newLevel3.html", counterLevel1=counterLevel1, counterLevel2=counterLevel2, counterLevel3=counterLevel3)

@app.route('/submit', methods=['POST'])
def submit():
    tabJsonLevel1 = []
    for x in range(1, maxNumberOfLevelsID):
        objectLevel1 = {}

        level1name = request.form.get(str(x) + 'Level1Nom', None)

        tablevel1keyword = []
        level1keyword = request.form.get(str(x) + 'Level1Keyword', None)
        if level1keyword:
            tablevel1keyword = level1keyword.split(',')

        level1action = request.form.get(str(x) + 'Level1Action', None)

        if level1name and tablevel1keyword:
            objectLevel1['level1Keywords'] = tablevel1keyword
            objectLevel1['level1Name'] = level1name
            if level1action:
                objectLevel1['level1Action'] = level1action
                tabJsonLevel1.append(objectLevel1)
            else:
                tabJsonLevel2 = []
                for y in range(1, maxNumberOfLevelsID):
                    objectLevel2 = {}
                    level2name = request.form.get(str(x) + 'Level1' + str(y) + 'Level2Nom', None)

                    tablevel2keyword = []
                    level2keyword = request.form.get(str(x) + 'Level1' + str(y) + 'Level2Keyword', None)
                    if level2keyword:
                        tablevel2keyword = level2keyword.split(',')

                    level2action = request.form.get(str(x) + 'Level1' + str(y) + 'Level2Action', None)

                    if level2name and tablevel2keyword:
                        objectLevel2['level2Name'] = level2name
                        objectLevel2['level2Keywords'] = tablevel2keyword
                        if level2action:
                            objectLevel2['level2Action'] = level2action
                            tabJsonLevel2.append(objectLevel2)

                        else:
                            tabJsonLevel3 = []
                            for z in range(1, maxNumberOfLevelsID):
                                objectLevel3 = {}
                                level3name = request.form.get(str(x) + 'Level1' + str(y) + 'Level2' + str(z) + 'Level3Nom', None)

                                tablevel3keyword = []
                                level3keyword = request.form.get(str(x) + 'Level1' + str(y) + 'Level2' + str(z) + 'Level3Keyword', None)
                                if level3keyword:
                                    tablevel3keyword = level3keyword.split(',')

                                level3action = request.form.get(str(x) + 'Level1' + str(y) + 'Level2' + str(z) + 'Level3Action', None)

                                if level3name and tablevel3keyword:
                                    objectLevel3['level3Name'] = level3name
                                    objectLevel3['level3Keywords'] = tablevel3keyword
                                    if level3action:
                                        objectLevel3['level3Action'] = level3action
                                        tabJsonLevel3.append(objectLevel3)

                                    else:
                                        print "level 4"
                            objectLevel2['level2level3'] = tabJsonLevel3
                            tabJsonLevel2.append(objectLevel2)
                objectLevel1['level1level2'] = tabJsonLevel2
                tabJsonLevel1.append(objectLevel1)
        print objectLevel1
    finalJson = json.dumps(tabJsonLevel1)
    return finalJson, 201
