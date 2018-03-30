#!/usr/bin/env python2

#author : Jing Guo jing.guo@colorado.edu
#name : Flask.py
#purpose :  The friendly GUI for novice users
#date : 2018.02.14
#version : 1.0.1
#version notes (latest): Compatible w/ python2. 

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import Markup
import os
import sys
import csv
import sqlite3
import traceback
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from multiprocessing import Process

app = Flask(__name__)

"""
cwd = os.getcwd()
separator = 'src/'
root_path = cwd.split(separator, 1)[0]
"""
#Unit Test Database
#DATABASE = root_path + "src/infrastructure/database/SUPERFREQ.db"


#Create a User home page and check our app flask is operational
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scanNetwork():
    return render_template('scan.html')

@app.route('/image')
def scanImage():
    return render_template('image.html')

app.route('/importCSV')
def importCSV():
    return render_template('importCSV.html')

app.route('/tests')
def runTests():
    return render_template('tests.html')

"""2.Using Chartjs
@app.route('/image', methods=["GET", "POST"])
def chart():
    print("\t Reading CSV File and Generating Graph... \n")
    #Create lists
    labels=[]
    values=[]

    #Check csv file
    if not os.path.isfile('WifiTest.csv'):
        print("\n The MCP has derezzed the file!\n")
        sys.exit()
        
    with open('WifiTest.csv') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            labels.append(row[3]+"-"+row[6])
            values.append(float(row[7]))
        print(labels)

    return render_template('image.html', labels=labels, values=values)"""

@app.route('/database', methods=["GET", "POST"])
def chart():
    db_path="../infrastructure/database/SUPERFREQ.db"
     
    if not os.path.isfile(db_path):
        HTMLoutput = "Unable to connect with SUPERFREQ database! The MCP has derezzed the file!"
    else:
        try:
            daba = sqlite3.connect(db_path)
            query = "SELECT * FROM Wifi"
            cursor = daba.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = ["duration","frame","subtype","ssid","seq_nr","mac_address_1", "mac_address_2", "mac_address_3", "frequency", "occurrence"]
            headers = ' '.join(item.rjust(20) for item in headers)
            HTMLformat = [headers]
            for row in rows:
                HTMLformat.append(' '.join(str(item).rjust(20) for item in row))
            HTMLoutput = '\n'.join(HTMLformat)
        except:
            HTMLoutput = "Database read error!"
            traceback.print_exc()    
                
        return(render_template('indexBlueprint.html', bodyText=Markup("<pre>"+HTMLoutput+"</pre>")))
 
    """#Create lists
    labels=[]
    values=[]
    db,cur = connection()
	cur.execute("SELECT name FROM  WHERE " +  + " ")"""


#Error handling function
@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def errorpage(e):
    return("something going wrong here")

    #Run main program
if __name__ == '__main__':
    app.debug = True
    try:
        app.run(host='127.0.0.1', port=7721)
    except:
        print("Host on 127.0.0.1, Port: 7721, is currently unavailable.")